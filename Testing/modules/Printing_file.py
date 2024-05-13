import os
import subprocess
from pathlib import Path

def read_file_content(file_path: str) -> bytes:
    """
    Reads the content of a file from the specified path and returns it.
    Args:
    file_path (str): The path of the file to read.
    Returns:
    bytes: The content of the file.
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
        return None
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def save_file_with_unique_number(content: bytes, folder_path: str, base_filename: str, file_type: str) -> str:
    """
    Saves a file to the specified folder with a unique consecutive number in the filename.
    Args:
    content (bytes): The content of the file.
    folder_path (str): The path to the folder where the file should be saved.
    base_filename (str): The base name of the file to save.
    file_type (str): The type of the file ('pdf' or 'docx').
    Returns:
    str: The full path to the saved file.
    """
    # Ensure the folder exists
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    # Determine the next available file number
    suffix = f".{file_type}"
    existing_files = [f for f in os.listdir(folder_path) if f.startswith(base_filename) and f.endswith(suffix)]
    numbers = [int(f[len(base_filename):-len(suffix)]) for f in existing_files if f[len(base_filename):-len(suffix)].isdigit()]
    next_number = max(numbers) + 1 if numbers else 1
    
    # Construct the file path with the unique number
    file_name = f"{base_filename}{next_number}{suffix}"
    file_path = os.path.join(folder_path, file_name)
    
    # Write the file
    with open(file_path, 'wb') as file:
        file.write(content)
    
    return file_path

def print_file(file_path: str) -> None:
    """
    Prints the file using the default printer.
    Args:
    file_path (str): The path to the file to be printed.
    """
    try:
        # Windows command to print files
        subprocess.run(['start', '', '/b', file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to print the file: {e}")

# Example usage:
if __name__ == "__main__":
    # User input for file type and file path
    file_type = input("Enter the file type ('pdf' or 'docx'): ").lower()
    file_path_input = input("Enter the full path to the file you want to save and print: ")

    if file_type not in ['pdf', 'docx']:
        print("Invalid file type entered.")
    else:
        # Read the content of the file provided by the user
        content = read_file_content(file_path_input)
        if content is not None:
            # Save and print the file
            try:
                folder_path = 'C:/path/to/save'
                base_filename = 'example'
                saved_file_path = save_file_with_unique_number(content, folder_path, base_filename, file_type)
                print_file(saved_file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
