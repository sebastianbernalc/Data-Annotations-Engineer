# Invoice Processing System

This project processes invoices using the Veryfi API and organizes the extracted data into JSON format. The system includes validation for PDF files, extraction of invoice information, and logging of operations.

## Code Paradigm

The project follows a modular design with separate files handling different aspects:

- **`main.py`**: The main entry point of the project. It runs the readInvoices() function that processes the invoices in the designated folder.
- **`Tools folder`**: Contains the tools and settings needed for validation, extraction, and logging of information.
- **`apiVerify.py`**: Handles communication with the Veryfi API to process documents and extract relevant information.
- **`functionsExtractInfo.py`**: Contains the classes and functions to structure and validate the information extracted from invoices.
- **`logger_config.py`**: Configures the logging system to capture and store events and errors that occur during execution.
- **`readInvoices.py`**: Iterates over the files in the invoices folder, validates them, and if valid, processes them using apiVerify.py.
- **`validationFiles.py`**: Contains the PDFValidator class that validates the existence and extension of PDF files.

  The project uses several classes to structure and validate the information:

   VendorInfo, BillToInfo, InvoiceInfo, LineItem: These classes in functionsExtractInfo.py represent the information extracted from invoices. Each class has a to_dict() method that converts the data into a dictionary for easy export to JSON.
  ```bash
  class VendorInfo:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):
        return {
            "vendor_name": self.name,
            "vendor_address": self.address,
        }
   ```
  PDFValidator: This class in validationFiles.py is responsible for validating that the files to be processed exist and have the correct extension (.pdf).
  ```bash
  class PDFValidator:
    def __init__(self, file_path, valid_extensions=['.pdf']):
        self.file_path = file_path
        self.valid_extensions = valid_extensions

    def validate(self):
        try:
            self.validate_file_exists()
            self.validate_file_extension()
            logger.info(f"The file {self.file_path} is valid and ready for processing.")
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            return False
        return True
  ```

  The project is designed to handle errors robustly using a logging system and custom exceptions:

   VeryfiClientError: A custom exception in apiVerify.py that handles specific errors related to interaction with the Veryfi API.
   
   ```bash
   class VeryfiClientError(Exception):
    """Custom exception for errors related to the Veryfi Client."""
    pass
   ```

  Exception Handling: The code catches different types of exceptions (FileNotFoundError, ValueError, JSONDecodeError, among others) and logs them to facilitate error diagnosis.
  ```bash
  except VeryfiClientError as e:
    logger.error(f"Error processing document with Veryfi: {e}")
   except json.JSONDecodeError as e:
       logger.error(f"Error decoding JSON response: {e}")
   except ValueError as e:
       logger.error(f"Validation error: {e}")
   except Exception as e:
       logger.error(f"An unexpected error occurred: {e}")
  ```

  The project uses the logging module to capture and store event logs at runtime. The logs are saved to a file called veryfi_process.log in the ./logs folder.

  The logger configuration is defined in logger_config.py, where both a file handler and a console handler are configured, allowing logs to be viewed in real time and stored for later review.
  
## Installation

To set up the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/invoice-processing-system.git
   ```
2. **Install**
   Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
   package manager for Python.
   
   
   Install the package from PyPI:
   ```bash
   pip install -U veryfi
   ```

3. **Getting Started**

   ### Obtaining Client ID and user keys
   If you don't have an account with Veryfi, please go ahead and register here: [https://hub.veryfi.com/signup/api/](https://hub.veryfi.com/signup/api/)
   
   ### Python API Client Library
   The **veryfi** library can be used to communicate with Veryfi API. All available functionality is described here https://veryfi.github.io/veryfi-python/reference/veryfi/#client
   
   Below is the sample script using **veryfi** to OCR and extract data from a document:

   ```python
   
   from veryfi import Client
   
   client_id = 'your_client_id'
   client_secret = 'your_client_secret'
   username = 'your_username'
   api_key = 'your_password'
   
   categories = ['Grocery', 'Utilities', 'Travel']
   file_path = '/tmp/invoice.jpg'
   
   # This submits document for processing (takes 3-5 seconds to get response)
   veryfi_client = Client(client_id, client_secret, username, api_key)
   response = veryfi_client.process_document(file_path, categories=categories)
   response
   ```
4. **Results**
   When you run the project, you will get several results organized in different folders and files, reflecting the processing of PDF invoices and log management.

   Processing PDF Invoices
   Location of Invoices: Invoices must be in the ./tmp/ folder.
   
   Processing Result:
   
   The data extracted from each PDF invoice will be saved in JSON files within the ./responses/ folder.
   The name of each JSON file will be the same as the corresponding PDF invoice, but with the .json extension.

   ```bash
   {
    "general_info": {
        "invoice_number": "1556267",
        "date": "2023-09-22 00:00:00",
        "vendor_name": "switch",
        "vendor_address": "PO Box 674592\nDallas, TX 75267-4592",
        "bill_to_name": "Toni Hackel"
    },
    "line_items": [
        {
            "sku": null,
            "description": "Transport | Switch Fiber Pair (Intra-campus) | Pairs (4419693704) (04/2023|10 Gbps Fiber\nto HOEpyb (YSPG4VFH) (04/2023)",
            "quantity": 2912.98,
            "tax_rate": null,
            "price": 934.09,
            "total": 2720985.49
        },
        {
            "sku": null,
            "description": "Carrier Taxes for Transport | 230 Gbps Wavelength Diverse between Sparks, OR 56789 and\nPlano, NV 98765 (SNpTfT) (NJYM5MQP) (07/2023 Taxes) (07/2023)",
            "quantity": 3500.87,
            "tax_rate": null,
            "price": 6229.33,
            "total": 21808074.52
        }
    ]
   }
   ```
   Each section (vendor_info, bill_to_info, invoice_info, line_items) represents different parts of the invoice, with their data organized in a structured and easily readable format.

   Execution Logs
   Log Location: Logs of the project execution are saved in the ./logs/ folder in a file called veryfi_process.log.
   
   Log Contents:
   
   The logs include information about file validation, interaction with the Veryfi API, data processing, and any errors or warnings that occur during execution.

   ```bash
   2024-08-29 21:41:33 - INFO - The file ./tmp/synth-switch_v5-14.pdf is valid and ready for processing.
   2024-08-29 21:41:33 - DEBUG - Starting new HTTPS connection (1): api.veryfi.com:443
   2024-08-29 21:41:41 - DEBUG - https://api.veryfi.com:443 "POST /api/v8/partner/documents/ HTTP/11" 201 30645
   2024-08-29 21:41:41 - INFO - The file ./tmp/synth-switch_v5-4.pdf is valid and ready for processing.
   2024-08-29 21:41:41 - DEBUG - Starting new HTTPS connection (1): api.veryfi.com:443
   2024-08-29 21:41:47 - DEBUG - https://api.veryfi.com:443 "POST /api/v8/partner/documents/ HTTP/11" 201 11257
   ```

   Error Handling
   
   Captured Errors
   
   - Errors that occur during file validation, API interaction, or data conversion are captured and logged.
   - Errors do not halt the entire execution of the project, allowing other invoices to be processed despite individual failures.
   
   Examples of Handled Errors
   
   - **FileNotFoundError:** Occurs when a PDF file is not found in the `./tmp/` folder.
   - **JSONDecodeError:** Occurs when the response from the Veryfi API is not a valid JSON.
   - **VeryfiClientError:** Happens when there is a specific issue with the Veryfi API.

   
