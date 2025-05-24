import os
import time
import pandas as pd
from docx import Document
from pathlib import Path
from win32com import client
from .base import Exporter


class PdfExporter(Exporter):
    def export(self, dataframe: pd.DataFrame, output_path: str):
        # Gera caminho absoluto e garante que diretório existe
        output_path = Path(output_path).resolve()
        temp_word_path = output_path.with_stem(f"{output_path.stem}_temp").with_suffix(".docx")
        Path(output_path.parent).mkdir(parents=True, exist_ok=True)

        try:
            # Cria o arquivo DOCX com a tabela
            doc = Document()
            section = doc.sections[0]
            section.orientation = 1  # 0 = portrait (padrão), 1 = landscape
            section.page_width, section.page_height = section.page_height, section.page_width  # Inverte largura/altura
            table = doc.add_table(rows=1, cols=len(dataframe.columns))
            table.style = 'Table Grid'

            # Adiciona cabeçalhos
            for i, column in enumerate(dataframe.columns):
                table.rows[0].cells[i].text = column

            # Adiciona linhas de dados
            for _, row in dataframe.iterrows():
                row_cells = table.add_row().cells
                for i, value in enumerate(row):
                    row_cells[i].text = str(value)

            doc.save(str(temp_word_path))
            print(f"📄 Word salvo: {temp_word_path}")

            # Inicia Microsoft Word via COM
            word = client.Dispatch("Word.Application")
            word.Visible = False
            word.DisplayAlerts = False

            doc_com = word.Documents.Open(str(temp_word_path))
            doc_com.Tables(1).Rows.First.HeadingFormat = True  # Ativa repetição da primeira linha da tabela

            # Cabeçalho fixo em todas as páginas
            for section in doc_com.Sections:
                header = section.Headers(1).Range
                header.Text = "Tabela do Memorial SIGEF"
                header.Font.Size = 10
                header.ParagraphFormat.Alignment = 1

            # Rodapé com número de página / total
            for section in doc_com.Sections:
                footer = section.Footers(1).Range
                footer.InsertBefore("Página ")
                footer.Collapse(0)
                footer.Fields.Add(footer, 33)
                footer.ParagraphFormat.Alignment = 1

            # Salva como PDF
            doc_com.SaveAs2(str(output_path), FileFormat=17)
            print(f"✅ PDF salvo: {output_path}")

            doc_com.Close(False)
            word.Quit()
            time.sleep(1)
        finally:
            if temp_word_path.exists():
                try:
                    os.remove(temp_word_path)
                    print(f"🗑️ Word temporário removido: {temp_word_path}")
                except PermissionError:
                    print(f"⚠️ Não foi possível remover o temporário. Feche manualmente: {temp_word_path}")
