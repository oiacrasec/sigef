from .base import Exporter
import pandas as pd

class WebExporter(Exporter):
    def export(self, dataframe: pd.DataFrame, output_path: str):
        html_content = dataframe.to_html(index=False, border=1, justify="center")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("<html><head><meta charset='UTF-8'><title>Memorial SIGEF</title></head><body>")
            f.write("<h1>Tabela do Memorial SIGEF</h1>")
            f.write(html_content)
            f.write("</body></html>")
        print(f"🌐 HTML salvo em: {output_path}")
