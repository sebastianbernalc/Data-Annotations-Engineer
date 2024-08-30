# Api_verify.py
import os
from veryfi import Client
import json
from Tools import functionsExtractInfo
from Tools.logger_config import logger

class VeryfiClientError(Exception):
    """Custom exception for errors related to the Veryfi Client."""
    pass

def extract_info(file_path):
    try:
        client_id = 'vrf8ZiY85FelZbUg8zutCVsf4ocLZNEh5U0ClNI'
        client_secret = 'jXoT2f9k75LM7AOOJJII4WsyradTiccvRP5Gk0rhPb7jmIFCS0rpokPlPuS2PddTVHOW5UyIsSRlYlbiaKxDstyKG28gIAiO34yuboNOctAA3CTdehtPzov8UvSjpk9Y'
        username = 'ljndrsebastian'
        api_key = '175ec84797675c266dbef42ede49a734'

        categories = ['Grocery', 'Utilities', 'Travel']

        veryfi_client = Client(client_id, client_secret, username, api_key)
        response = veryfi_client.process_document(file_path, categories=categories)

        structured_data = {
            "general_info": functionsExtractInfo.extract_general_info(response),
            "line_items": functionsExtractInfo.extract_line_items(response)
        }

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join('./responses', f'{base_name}.json')
        with open(output_file, 'w') as json_file:
            json.dump(structured_data, json_file, indent=4)

    except VeryfiClientError as e:
        logger.error(f"Error processing document with Veryfi: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response: {e}")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
