# factories/pe4_extractor.py
from .table_extractor_factory import TableExtractorFactory
from extractors.pe4_table_extractor import PE4TableExtractor

class PE4ExtractorFactory(TableExtractorFactory):
    def create_extractor(self):
        return PE4TableExtractor()
