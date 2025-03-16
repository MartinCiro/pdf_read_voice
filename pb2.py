from pydub import AudioSegment
from pydub.playback import _play_with_pyaudio
from piper import PiperVoice
import threading
import io
import time

from pb import PDFReader

class AudioPlayer:
    def __init__(self, text, voice_model):
        """Inicializa el reproductor con el texto y la voz de Piper."""
        self.voice = PiperVoice.load(*voice_model)  
        self.audio_stream = self.voice.synthesize_stream_raw(text)
        self.audio_data = b''.join(self.audio_stream)

        self.audio_buffer = io.BytesIO(self.audio_data)
        self.original_audio = AudioSegment.from_raw(
            self.audio_buffer, 
            sample_width=2,   # 16 bits = 2 bytes
            frame_rate=22050, # Frecuencia por defecto en Piper
            channels=1        # Mono
        )

        self.audio = self.original_audio  # Audio con velocidad modificada
        self.current_position = 0
        self.is_playing = False
        self.speed = 1.0

    def _apply_speed(self):
        """Aplica el cambio de velocidad sin distorsión."""
        if self.speed > 5:
            self.speed = 1  # Si la velocidad es mayor a 5, la dejamos en 1x
        
        print(f"Cambiando la velocidad a {self.speed}x")

        self.audio = self.original_audio.speedup(playback_speed=self.speed)

        print(f"Nueva duración: {self.audio.duration_seconds} segundos")

    def play_pause(self):
        """Método unificado para reproducir o pausar el audio."""
        if self.is_playing:
            self.is_playing = False
        else:
            self.is_playing = True
            threading.Thread(target=self._play_audio, daemon=True).start()

    def _play_audio(self):
        """Función interna para manejar la reproducción con pydub."""
        while self.is_playing and self.current_position < len(self.audio):
            chunk = self.audio[self.current_position:self.current_position + 1000]
            _play_with_pyaudio(chunk)
            self.current_position += 1000
            time.sleep(1 / self.speed)

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
        print(f"🔄 Velocidad cambiada a {self.speed}x")

    def page_next(self):
        """Avanza una página (asumiendo 30s por página)."""
        self.current_position = min(len(self.audio), self.current_position + 30000)

    def page_prev(self):
        """Retrocede una página (asumiendo 30s por página)."""
        self.current_position = max(0, self.current_position - 30000)

    def save_audio(self, output_path="output.mp3"):
        """Guarda el audio generado en un archivo."""
        self.audio.export(output_path, format="mp3")
        print(f"✅ Audio guardado en: {output_path}")

# Uso del reproductor
pdf_path = "vendor/pdf/prueba.pdf"
reader = PDFReader(pdf_path)
text = reader.extract_text()

voice_model = ("vendor/voice/mx/espeak_es.onnx", "vendor/voice/mx/espeak_es.json")

player = AudioPlayer(text, voice_model)

# Pruebas de reproducción y cambio de velocidad
player.play_pause()  # Inicia
time.sleep(3)
player.change_speed(3)  # Velocidad 2x
time.sleep(5)
player.retrocede_five()  # Velocidad 1x
player.play_pause()
#player.play_pause()  # Pausa

# Guardar el audio generado
player.save_audio("mi_audio.mp3")
player.play_pause()
