# Invoice Processing System

This project processes invoices using the Veryfi API and organizes the extracted data into JSON format. The system includes validation for PDF files, extraction of invoice information, and logging of operations.

## Code Paradigm

The project follows a modular design with separate files handling different aspects:

- **`apiVerify.py`**: Interacts with the Veryfi API to process documents and extract information.
- **`functionsExtractInfo.py`**: Contains classes and functions for validating and extracting information from the API response.
- **`logger_config.py`**: Configures logging to capture and store log messages.
- **`readInvoices.py`**: Reads and validates PDF files from a directory and triggers extraction if the files are valid.
- **`validationFiles.py`**: Provides validation functionality for checking file existence and extensions.
- **`Main.py`**: The entry point for the application, which triggers the reading and processing of invoices.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/invoice-processing-system.git
