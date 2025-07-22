import json
import os
from utils.logger import logger

def write_local_json(data, output_path, file_name):
    try:
        os.makedirs(output_path, exist_ok=True)
        with open(os.path.join(output_path, f"{file_name}_transformed.json"), "w") as f:
            json.dump(data, f, indent=2)
        logger.info(f"Written {file_name}_transformed.json")
    except Exception as e:
        logger.error(f"Write error: {e}")
