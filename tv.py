import pyttsx3
from pydub import AudioSegment
import tempfile
import os

# Inicializar el motor de pyttsx3
engine = pyttsx3.init()

# Establecer propiedades del motor (opcional)
engine.setProperty('rate', 90)  # Velocidad de la voz
engine.setProperty('volume', 1)  # Volumen

# Función para generar el audio del texto y guardarlo en un archivo
def generar_audio(texto, archivo_salida):
    # Crear un archivo temporal en formato wav
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        temp_filename = tmp_file.name
        engine.save_to_file(texto, temp_filename)
        engine.runAndWait()
        
        # Convertir el archivo wav a mp3 usando pydub
        audio = AudioSegment.from_wav(temp_filename)
        audio.export(archivo_salida, format='mp3')
        
        # Eliminar el archivo temporal
        os.remove(temp_filename)

# Texto a convertir
texto = "Hola, este es un ejemplo de cómo generar un archivo de audio desde texto. No quiero no quienjfdlksjflksdjlkfjlskadflksadj"

# Generar el archivo de audio y guardarlo como archivo mp3
archivo_salida = "audio_generado.mp3"
generar_audio(texto, archivo_salida)

print(f"El archivo de audio se ha guardado como {archivo_salida}")
