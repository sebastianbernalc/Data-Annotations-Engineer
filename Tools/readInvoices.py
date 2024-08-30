import os
from Tools import validationFiles
from Tools import apiVerify
from Tools.logger_config import logger

def readInvoices():
    folder_path = './tmp/'  # Replace with the actual folder path

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            validator = validationFiles.PDFValidator(file_path)
            is_valid = validator.validate()

            if is_valid:
                apiVerify.extract_info(file_path)
            else:
                logger.error("One or more validations failed.")
