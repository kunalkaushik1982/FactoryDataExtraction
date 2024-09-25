# factories/table_extractor_factory.py
from abc import ABC, abstractmethod

class TableExtractorFactory(ABC):
    @abstractmethod
    def create_extractor(self):
        pass
