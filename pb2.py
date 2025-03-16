from pydub import AudioSegment
from piper import PiperVoice
from pb import PDFReader
import io
import wave

# Cargar el modelo de voz desde los archivos
voice = PiperVoice.load("espeak_es.onnx", "espeak_es.json")

pdf_path = "/home/ciro/Descargas/pb.pdf"  # Ruta de tu archivo PDF
reader = PDFReader(pdf_path)

# Texto a convertir en audio
text = reader.extract_text()

# Generar el audio como un flujo de datos
audio_stream = voice.synthesize_stream_raw(text)

# Crear un objeto BytesIO para manejar el flujo de datos en memoria
audio_buffer = io.BytesIO()

# Guardar el audio como un archivo WAV en el buffer de memoria
with wave.open(audio_buffer, "wb") as f:
    f.setnchannels(1)       # Mono
    f.setsampwidth(2)       # 16 bits
    f.setframerate(22050)   # Tasa de muestreo (ajústala según el modelo)
    
    # Escribir los datos en el buffer en lugar de un archivo físico
    for chunk in audio_stream:
        f.writeframes(chunk)

# Volver al principio del buffer para leerlo y convertirlo a MP3
audio_buffer.seek(0)

# Convertir el buffer WAV directamente a MP3 usando pydub
audio = AudioSegment.from_wav(audio_buffer)

# Exportar el MP3 directamente a un archivo
audio.export("output.mp3", format="mp3")

print("✅ Audio generado correctamente: output.mp3")
