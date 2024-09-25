# extractors/landscape_table_extractor.py
import pdfplumber

from .base_table_extractor import BaseTableExtractor
from utils.logger import log_exception

class LandscapeTableExtractor(BaseTableExtractor):
    def __init__(self):
        self.start_text = "2 Landscape"
        self.end_text = "End of Landscape"

    @log_exception
    def extract_table(self, pdf_file):
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if self.start_text in text and self.end_text in text:
                    # Extract landscape table logic
                    tables = page.extract_tables()
                    print("Extracted Landscape Table:", tables)
                    return tables
