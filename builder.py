import pandas as pd
from typing import List
from model import VerticeRegistro

class VerticeTableBuilder:
    def __init__(self, vertices: List[VerticeRegistro]):
        self.vertices = vertices

    def build_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([v.to_dict() for v in self.vertices])
