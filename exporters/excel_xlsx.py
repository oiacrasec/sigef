import pandas as pd
from .base import Exporter

class ExcelExporter(Exporter):
    def export(self, dataframe: pd.DataFrame, output_path: str):
        dataframe.to_excel(output_path, index=False)
        print(f"✅ Excel salvo em: {output_path}")
