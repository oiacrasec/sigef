import pandas as pd
from docx import Document
from .base import Exporter

class WordExporter(Exporter):
    def export(self, dataframe: pd.DataFrame, output_path: str):
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

        doc.save(output_path)
        print(f"📄 Word salvo em: {output_path}")
