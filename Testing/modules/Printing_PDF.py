import os
import subprocess
from pathlib import Path
from config import validate_file_path
import config

def save_pdf_with_unique_number(content: bytes, folder_path: str, base_filename: str) -> str:
    """
    Saves a PDF file to the specified folder with a unique consecutive number in the filename.
    Args:
    content (bytes): The content of the PDF file.
    folder_path (str): The path to the folder where the PDF should be saved.
    base_filename (str): The base name of the PDF file to save.
    Returns:
    str: The full path to the saved PDF file.
    """
    # Ensure the folder exists
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    # Determine the next available file number
    existing_files = [f for f in os.listdir(folder_path) if f.startswith(base_filename) and f.endswith('.pdf')]
    numbers = [int(f[len(base_filename):-4]) for f in existing_files if f[len(base_filename):-4].isdigit()]
    next_number = max(numbers) + 1 if numbers else 1
    
    # Construct the file path with the unique number
    file_name = f"{base_filename}{next_number}.pdf"
    file_path = os.path.join(folder_path, file_name)
    
    # Write the PDF file
    with open(file_path, 'wb') as file:
        file.write(content)
    
    return file_path

def print_pdf(file_path: str) -> None:
    """
    Prints the PDF file using the default printer.
    Args:
    file_path (str): The path to the PDF file to be printed.
    """
    try:
        # Windows command to print PDF files
        subprocess.run(['start', '', '/b', file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to print the PDF: {e}")


pdf_save = config['paths']['PDF_SAVE']
validate_file_path(pdf_save)

pdf_input = config['paths']['PDF_INPUT']
validate_file_path(pdf_input)

# Example usage:
if __name__ == "__main__":
    with open(pdf_input, 'rb') as file:
        pdf_content = file.read()  # Read the entire file as a byte string
    # Save and print the PDF
    try:
        pdf_path = save_pdf_with_unique_number(pdf_content, pdf_save, 'example_')
        print_pdf(pdf_path)
    except Exception as e:
        print(f"An error occurred: {e}")
