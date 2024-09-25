
import yaml
#from utils.logger import log_exception

class ConfigInfo:
    # Image output folder
    IMAGE_OUTPUT_FOLDER = "extracted_images"

    # Table extraction parameters
    START_TEXT = "Performance Indicators for"
    END_TEXT = "2 Landscape"
    REQUIRED_COLUMNS = ["Area", "Indicators", "Value", "Trend"]

    # Logging
    LOG_FILE = "process.log"

    def load_config(path):
            with open(path, 'r') as file:
                config = yaml.safe_load(file)
            return config    