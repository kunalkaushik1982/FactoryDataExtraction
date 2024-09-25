# FactoryDataExtraction

project/
├── factories/
│   ├── table_extractor_factory.py  # Abstract Factory Interface
│   ├── pe4_extractor.py            # Concrete Factory for PE4 table
│   ├── landscape_extractor.py      # Concrete Factory for Landscape table
├── extractors/
│   ├── base_table_extractor.py     # Abstract Base Extractor Class
│   ├── pe4_table_extractor.py      # PE4 Table Extractor Class
│   ├── landscape_table_extractor.py # Landscape Table Extractor Class
├── config/
│   ├── config.yaml                 # Configuration file for start/end texts and paths
├── main.py                         # Main script to run extraction
├── utils/
│   ├── image_extractor.py          # Image Extraction Helper
│   ├── logger.py                   # Logger and Exception Handling
└── README.md
