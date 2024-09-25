# extractors/pe4_table_extractor.py
import pdfplumber
import pandas as pd
import re
import yaml

from .base_table_extractor import BaseTableExtractor
from utils.logger import log_exception
from utils.config import ConfigInfo

class PE4TableExtractor(BaseTableExtractor):
    def __init__(self):
        path=r"C:\Users\kunkaush1\Documents\Project\FactoryDataExtraction\utils\config.yaml"
        self.config = ConfigInfo.load_config(path)
        self.start_text = self.config['pe4_table_extractors']['start_text']
        self.end_text = self.config['pe4_table_extractors']['end_text']  # No specific end text in this case
    
    @log_exception
    def extract_table(self, pdf_file):      
        required_columns= self.config['pe4_table_extractors']['columns']
        data = []
        extraction_zone = False  # Flag to start extraction between start_text and end_text
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if self.start_text in text:
                    extraction_zone = True 
                    
                    if extraction_zone:
                        tables = page.extract_tables()
                        for table in tables:
                            if len(table) > 0:
                                first_row_cleaned = [' '.join(col.replace("\n", " ").split()).strip() if col else '' for col in table[0]]
                                
                                if all(req_col in first_row_cleaned for req_col in required_columns):
                                    # self.logger.log_info(f"Valid table found on page {page.page_number}")
                                    
                                    for row in table[1:]:
                                        if len(row) == len(required_columns):
                                            row_cleaned = [' '.join(col.replace("\n", " ").split()).strip() if col else '' for col in row]
                                            data.append(row_cleaned)

                    if self.end_text in text and extraction_zone:
                        break  # Stop processing further pages once end_text is found

            df = pd.DataFrame(data, columns=required_columns)
            return df
                 
                
    @log_exception
    def extract_sap_info(self, pdf_file):
        """Extract 'SAP System ID', 'Analysis from', and 'Until' values from the first page of the PDF."""
        with pdfplumber.open(pdf_file) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            
            # Extract SAP System ID
            sap_id_match = re.search(r"SAP System ID\s+(\S+)", text)            
            sap_id = sap_id_match.group(1) if sap_id_match else "Unknown"
            
            # Extract "Analysis from" and "Until" dates
            analysis_from_match = re.search(r"Analysisfrom\s+(\S+)", text)            
            until_match = re.search(r"Until\s+(\S+)", text)
            

            analysis_from = analysis_from_match.group(1) if analysis_from_match else "Unknown"           
            until_date = until_match.group(1) if until_match else "Unknown"
            

            # Concatenate for the sheet name
            sheet_name = f"{sap_id}-{analysis_from}-{until_date}"
            

            return sheet_name
        

    