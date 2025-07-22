from input_reader.local_reader import read_local_json_files
from output_writer.local_writer import write_local_json
from transformer.data_transformer import transform_user
from config import settings
from utils.logger import logger

def main():
    try:
        logger.info("Starting transformation (local)...")
        users = read_local_json_files(settings.INPUT_DIR)
        for idx, user in enumerate(users):
            transformed = transform_user(user)
            if transformed:
                write_local_json(transformed, settings.OUTPUT_DIR, f"user_{idx}")
        logger.info("Transformation completed (local).")
    except Exception as e:
        logger.exception(f"Failed main execution: {e}")

if __name__ == "__main__":
    main()
