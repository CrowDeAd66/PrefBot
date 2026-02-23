import pdfplumber

class PDFParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        with pdfplumber.open(self.file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            return text

    def extract_tables(self):
        with pdfplumber.open(self.file_path) as pdf:
            tables = []
            for page in pdf.pages:
                tables.extend(page.extract_tables())
            return tables

    def detect_empenho_data(self):
        with pdfplumber.open(self.file_path) as pdf:
            empenho_data = []
            for page in pdf.pages:
                # Replace the following line with actual logic to detect "empenho" data
                text = page.extract_text() or ''
                if 'empenho' in text:
                    empenho_data.append(text)
            return empenho_data
