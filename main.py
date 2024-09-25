# main.py
import os
import argparse
import pandas as pd
from factories.pe4_extractor import PE4ExtractorFactory
from factories.landscape_extractor import LandscapeExtractorFactory
from utils.logger import log_exception

@log_exception
def extract_tables_from_pdfs(input_folder, output_file):
    pe4_factory = PE4ExtractorFactory()
    landscape_factory = LandscapeExtractorFactory()

    pe4_extractor = pe4_factory.create_extractor()
    landscape_extractor = landscape_factory.create_extractor()

    all_df = []
    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, pdf_file)
            
            pe4_df = pe4_extractor.extract_table(pdf_path)
            # pe4_table = pe4_extractor.extract_table(pdf_path)
            # landscape_table = landscape_extractor.extract_table(pdf_path)

            if not pe4_df.empty:
                sheet_name = pe4_extractor.extract_sap_info(pdf_path)
                all_df.append((sheet_name, pe4_df))
            # if landscape_table:
            #     all_tables.append(("Landscape Table", landscape_table))

    # Save to Excel with separate sheets
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, dataframe in all_df:            
            dataframe.to_excel(writer, sheet_name=sheet_name,index=False)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="PDF Table Extractor")
    # parser.add_argument("--input_folder", type=str, required=True, help="Folder containing input PDF files")
    # parser.add_argument("--output_file", type=str, required=True, help="Output Excel file path")
    # args = parser.parse_args()
    # extract_tables_from_pdfs(args.input_folder, args.output_file)

    input_folder=r"C:\Users\kunkaush1\Documents\Project\FactoryDataExtraction\Data"
    output_file=r"C:\Users\kunkaush1\Documents\Project\FactoryDataExtraction\Data\excel.xlsx"
    extract_tables_from_pdfs(input_folder, output_file)
