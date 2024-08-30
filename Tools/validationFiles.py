import os
from Tools.logger_config import logger


class PDFValidator:
    def __init__(self, file_path, valid_extensions=['.pdf']):
        self.file_path = file_path
        self.valid_extensions = valid_extensions

    def validate_file_exists(self):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file at path {self.file_path} does not exist.")
        return True

    def validate_file_extension(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext not in self.valid_extensions:
            raise ValueError(f"Invalid file extension: {ext}. Expected one of {self.valid_extensions}.")
        return True

    def validate(self):
        try:
            self.validate_file_exists()
            self.validate_file_extension()
            logger.info(f"The file {self.file_path} is valid and ready for processing.")
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            return False
        return True