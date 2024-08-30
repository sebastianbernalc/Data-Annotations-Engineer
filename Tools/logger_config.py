import logging
import os

def setup_logger():
    """Configura y devuelve el logger."""
    log_directory = './logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_file_path = os.path.join(log_directory, 'veryfi_process.log')
    
    # Crear el logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Nivel de logs a capturar

    # Crear manejador de archivo
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)  # Nivel de logs para el archivo

    # Crear manejador de consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Nivel de logs para la consola

    # Crear y establecer formato de los logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Añadir manejadores al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Crear el logger y configurarlo
logger = setup_logger()
