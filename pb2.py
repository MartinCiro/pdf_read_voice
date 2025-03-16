from pydub import AudioSegment
from piper import PiperVoice
from pb import PDFReader
import io

# Cargar el modelo de voz
voice = PiperVoice.load("vendor/voice/mx/espeak_es.onnx", "vendor/voice/mx/espeak_es.json")

# Cargar el texto desde el PDF
pdf_path = "vendor/pdf/prueba.pdf"
reader = PDFReader(pdf_path)
text = reader.extract_text()

# Generar el audio como un flujo de datos (bytes crudos)
audio_stream = voice.synthesize_stream_raw(text)
audio_data = b''.join(audio_stream)  # Convertir el generador en bytes

# Crear un buffer de memoria para el audio
audio_buffer = io.BytesIO(audio_data)

# Convertir el audio PCM crudo directamente a un objeto pydub.AudioSegment
audio = AudioSegment.from_raw(
    audio_buffer, 
    sample_width=2,   # 16 bits = 2 bytes
    frame_rate=22050, # 22050 Hz (frecuencia de muestreo por defecto en piper)
    channels=1        # Mono
)

# Exportar directamente a MP3 sin generar WAV
mp3_path = "output.mp3"
audio.export(mp3_path, format="mp3")

print(f"✅ Audio generado correctamente: {mp3_path}")
