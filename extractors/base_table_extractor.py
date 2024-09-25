# extractors/base_table_extractor.py
from abc import ABC, abstractmethod

class BaseTableExtractor(ABC):
    @abstractmethod
    def extract_table(self, pdf_file):
        pass
