import os
import pandas as pd
from docx import Document
from docx2pdf import convert
from .base import Exporter


class PdfExporter(Exporter):
    def export(self, dataframe: pd.DataFrame, output_path: str):
        temp_word_path = output_path.replace(".pdf", ".docx")
        try:
            doc = Document()
            doc.add_heading("Tabela do Memorial SIGEF", 0)

            table = doc.add_table(rows=1, cols=len(dataframe.columns))
            table.style = 'Table Grid'

            for i, column in enumerate(dataframe.columns):
                table.rows[0].cells[i].text = column

            for _, row in dataframe.iterrows():
                row_cells = table.add_row().cells
                for i, value in enumerate(row):
                    row_cells[i].text = str(value)

            doc.save(temp_word_path)
            print(f"📄 Documento Word (temporário) salvo em: {temp_word_path}")
            convert(temp_word_path, output_path)
            print(f"📄 PDF final salvo em: {output_path}")
        finally:
            if os.path.exists(temp_word_path):
                os.remove(temp_word_path)
