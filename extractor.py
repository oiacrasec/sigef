import pdfplumber
import re
from typing import List
from model import VerticeRegistro

class MemorialPDFExtractor:
    def __init__(self, path_pdf: str):
        self.path_pdf = path_pdf

    def extract(self) -> List[VerticeRegistro]:
        resultados = []
        with pdfplumber.open(self.path_pdf) as pdf:
            for page in pdf.pages:
                for line in page.extract_text().split('\n'):
                    match = self._match_line(line)
                    if match:
                        resultados.append(VerticeRegistro(*match))
        return resultados

    def _match_line(self, line: str):
        regex = r'([A-Z0-9\-]+)\s+(-?\d+°\d+\'\d+,\d+")\s+(-?\d+°\d+\'\d+,\d+")\s+([\d,]+)\s+([A-Z0-9\-]+)\s+([\d°\' ]+)\s+([\d,]+)\s+(.+)'
        match = re.match(regex, line)
        if match:
            return match.groups()
        return None
