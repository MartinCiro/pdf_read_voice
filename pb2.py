from pydub import AudioSegment
from piper import PiperVoice
from pb import PDFReader
import io
import wave

# Cargar el modelo de voz desde los archivos
voice = PiperVoice.load("espeak_es.onnx", "espeak_es.json")

pdf_path = "padre.pdf"  # Ruta de tu archivo PDF
reader = PDFReader(pdf_path)

# Texto a convertir en audio
text = reader.extract_text()

# Generar el audio como un flujo de datos
audio_stream = voice.synthesize_stream_raw(text)

# Crear un objeto BytesIO para manejar el flujo de datos en memoria
audio_buffer = io.BytesIO()
# Utilizamos pydub para manejar los datos del audio y convertirlo a MP3
audio = AudioSegment.from_file(io.BytesIO(b''.join(audio_stream)), format="wav")

# Exportar el MP3 directamente a un archivo
audio.export("output.mp3", format="mp3")

print("✅ Audio generado correctamente: output.mp3")