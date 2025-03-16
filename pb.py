import fitz  # pymupdf

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""

    def extract_text(self):
        """Lee y extrae el texto de un archivo PDF."""
        try:
            pdf_document = fitz.open(self.file_path)  # Abrir el PDF
            self.text = "\n".join([pdf_document.load_page(i).get_text() for i in range(pdf_document.page_count)])
            return self.text
        except Exception as e:
            print(f"Error al leer el PDF: {e}")
            return None

