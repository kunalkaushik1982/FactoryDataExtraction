# factories/landscape_extractor.py
from .table_extractor_factory import TableExtractorFactory
from extractors.landscape_table_extractor import LandscapeTableExtractor

class LandscapeExtractorFactory(TableExtractorFactory):
    def create_extractor(self):
        return LandscapeTableExtractor()
