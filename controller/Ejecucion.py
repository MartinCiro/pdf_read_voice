# ===========================================================================
# Importaciones de clases y librerias necesarias en esta vista
# ===========================================================================
# Region - Importación de librerias y clases.
import io
import time
import threading
from piper import PiperVoice
from pydub import AudioSegment
from controller.utils.Helpers import Helpers
import customtkinter as ctk
from pydub.playback import _play_with_pyaudio
from tkinter import messagebox
# Endregion - Importación de librerias y clases.

# Region - Inicialización de clases para uso de metodos.
helpers = Helpers()
# Endregion - Inicialización de clases para uso de metodos.

# Clase pivote para realizar la ejecución del bot. 
class AudioPlayer:
    def __init__(self, text_widget=None):
        """
        Constructor de la clase, se inicializarán las
        variables a utilizar dentro de la base de datos
        y se re asignaran sus valores luego de que se
        complete el formulario.
        """
        self.text = ""  # Texto a reproducir
        self.voice = None  # Modelo de voz
        self.audio = None  # Audio procesado
        self.original_audio = None  # Audio sin modificaciones
        self.audio_buffer = None  # Buffer de audio
        self.current_position = 0  # Posición en el audio
        self.is_playing = False  # Estado de reproducción
        self.speed = 1.0  # Velocidad de reproducción
        self.text_widget = text_widget 
        
    def inicialize(self, text, voice_model, textbx = None):
        """Inicializa el reproductor con el texto y la voz de Piper."""
        self.voice = PiperVoice.load(*voice_model)  
        self.audio_stream = self.voice.synthesize_stream_raw(text)
        self.audio_data = b''.join(self.audio_stream)

        self.audio_buffer = io.BytesIO(self.audio_data)
        self.original_audio = AudioSegment.from_raw(
            self.audio_buffer, 
            sample_width = 2,   
            frame_rate = 22050, 
            channels = 1       
        )

        self.audio = self.original_audio  # Audio con velocidad modificada
        self.current_position = 0
        self.is_playing = False
        self.speed = 1.0

        if textbx:
            self.text_widget = textbx

    def _apply_speed(self):
        """Aplica el cambio de velocidad sin distorsión."""
        if self.speed > 5:
            self.speed = 1  # Si la velocidad es mayor a 5, la dejamos en 1x
        
        print(f"Cambiando la velocidad a {self.speed}x")

        self.audio = self.original_audio.speedup(playback_speed=self.speed)

        print(f"Nueva duración: {self.audio.duration_seconds} segundos")

    def play_pause(self):
        """Reproduce o pausa el audio permitiendo actualizar el texto antes de reproducirlo."""
        if self.is_playing:
            self.is_playing = False  # Pausa la reproducción sin reiniciar
        else:
            # **Obtener siempre el texto más reciente**
            if self.text_widget:
                nuevo_texto = self.text_widget.get(1.0, ctk.END).strip()
            else:
                nuevo_texto = ""

            if not nuevo_texto:
                messagebox.showinfo("Aviso", "No hay texto para leer.")
                return

            # **Si el texto cambió, regenerar el audio**
            if nuevo_texto != self.text:
                self.text = nuevo_texto  # Guardar el nuevo texto
                path_inicial = helpers.getRoutes("FolderVoice", "Value")
                voice_model = (f"{path_inicial}/mx/espeak_es.onnx", f"{path_inicial}/mx/espeak_es.json")
                self.inicialize(self.text, voice_model)
                self.current_position = 0  # Reiniciar reproducción si el texto cambió

            self.is_playing = True

            # **Iniciar un solo hilo de reproducción**
            if not hasattr(self, "play_thread") or not self.play_thread.is_alive():
                self.play_thread = threading.Thread(target=self._play_audio, daemon=True)
                self.play_thread.start()


    def _play_audio(self):
        """Genera y reproduce el audio directamente desde el texto del Textbox."""
        try:
            # Obtener el texto actualizado del Textbox si está asignado
            if self.text_widget:
                self.text = self.text_widget.get(1.0, ctk.END).strip()

            # Validar si hay texto para reproducir
            if not self.text:
                messagebox.showinfo("Aviso", "No hay texto para leer.")
                return

            # Re-generar el audio con el nuevo texto antes de reproducir
            path_inicial = helpers.getRoutes("FolderVoice", "Value")
            voice_model = (f"{path_inicial}/mx/espeak_es.onnx", f"{path_inicial}/mx/espeak_es.json")

            self.inicialize(self.text, voice_model)  # Generar la síntesis de voz

            # Iniciar reproducción desde el principio
            self.current_position = 0
            self.is_playing = True

            # Bucle de reproducción
            while self.is_playing and self.current_position < len(self.audio):
                chunk = self.audio[self.current_position:self.current_position + int(1000 / self.speed)]
                _play_with_pyaudio(chunk)  # Reproduce el fragmento
                self.current_position += int(1000 / self.speed)
                time.sleep(1 / self.speed)

        except Exception as e:
            messagebox.showerror("Error", f"No ha sido posible reproducir el audio: {str(e)}")


    def avanza_five(self):
        """Avanza 5 segundos en el audio."""
        self.current_position = min(len(self.audio), self.current_position + 5000)

    def retrocede_five(self):
        """Retrocede 5 segundos en el audio."""
        self.current_position = max(0, self.current_position - 5000)

    def change_speed(self, speed):
        print(f"🔄 Cambiando la velocidad a {speed}x")
        """Cambia la velocidad de reproducción y ajusta el frame_rate."""
        self.speed = max(1.0, min(speed, 5.0))
        self._apply_speed()
        self.current_position = 0  # Reiniciar la posición al cambiar la velocidad
        print(f"🔄 Velocidad cambiada a {self.speed}x")

    def page_next(self):
        """Avanza una página (asumiendo 30s por página)."""
        self.current_position = min(len(self.audio), self.current_position + 30000)

    def page_prev(self):
        """Retrocede una página (asumiendo 30s por página)."""
        self.current_position = max(0, self.current_position - 30000)

    def save_audio(self, output_path="output.mp3"):
        """Guarda el audio generado en un archivo."""
        if self.audio:
            self.audio.export(output_path, format="mp3")
            print(f"✅ Audio guardado en: {output_path}")
        else:
            print("⚠ No hay audio generado para guardar.")

    