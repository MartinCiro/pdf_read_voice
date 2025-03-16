import wave
from piper import PiperVoice
from pb import PDFReader

# Cargar el modelo de voz desde los archivos
voice = PiperVoice.load("espeak_es.onnx", "espeak_es.json")

pdf_path = "/home/ciro/Descargas/pb.pdf"  # Ruta de tu archivo PDF
reader = PDFReader(pdf_path)

# Texto a convertir en audio
text = reader.extract_text()

# Generar el audio como un flujo de datos
audio_stream = voice.synthesize_stream_raw(text)

# Guardar el audio en formato WAV válido
with wave.open("output.wav", "wb") as f:
    f.setnchannels(1)       # Mono
    f.setsampwidth(2)       # 16 bits
    f.setframerate(22050)   # Tasa de muestreo (ajústala según el modelo)

    for chunk in audio_stream:
        f.writeframes(chunk)

print("✅ Audio generado correctamente: output.wav")
