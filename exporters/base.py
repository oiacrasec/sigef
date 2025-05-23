from abc import ABC, abstractmethod
import pandas as pd

class Exporter(ABC):
    @abstractmethod
    def export(self, dataframe: pd.DataFrame, output_path: str):
        pass
