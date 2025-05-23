from .excel_xlsx import ExcelExporter
from .word_docx import WordExporter
from .base import Exporter

class ExporterFactory:
    @staticmethod
    def get_exporter(formato: str) -> Exporter:
        match formato.lower():
            case "excel" | "xlsx":
                return ExcelExporter()
            case "word" | "docx":
                return WordExporter()
            case _:
                raise ValueError(f"Formato não suportado: {formato}")
