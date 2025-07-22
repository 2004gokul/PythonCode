import json
import os
from utils.logger import logger

def read_local_json_files(input_path):
    data = []
    for file in os.listdir(input_path):
        if file.endswith('.json'):
            try:
                with open(os.path.join(input_path, file)) as f:
                    data.append(json.load(f))
            except Exception as e:
                logger.error(f"Error reading {file}: {e}")
    return data
