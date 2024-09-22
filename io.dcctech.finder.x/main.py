import os
import re
import subprocess
import sys
from contextlib import nullcontext


def open_matching_files(directory, convert_to_int, *file_names):
    """
    Opens matching files in the specified directory based on the provided file names.
    If 'convert_to_int' is True, file names are processed as integers.

    :param directory: Directory to search for files.
    :param convert_to_int: Boolean indicating whether to convert file names to integers.
    :param file_names: List of file names to match.
    """

    # Iterate over each file in the specified directory
    for filename in os.listdir(directory):
        # Get the base name of the file (without extension)
        base_name, _ = os.path.splitext(filename)

        # If conversion to int is requested, attempt to convert the base name
        if convert_to_int:
            try:
                base_name = int(re.sub(r'\D', '', base_name))  # Remove non-digit characters
            except ValueError:
                continue  # Skip this file if conversion fails

        # Check each target file name provided by the user
        for target in file_names:
            # Convert target file names to integers if needed
            if convert_to_int:
                try:
                    target = int(re.sub(r'\D', '', target))
                except ValueError:
                    continue  # Skip this target if conversion fails

            # Check if the base name matches the target name
            if str(base_name) == str(target):
                file_path = os.path.join(directory, filename)  # Construct the full file path

                # Check if the file is a PDF
                if filename.lower().endswith('.pdf'):
                    print(f"Opening PDF in full screen: {file_path}")

                    # Open the PDF with the default viewer based on the OS
                    if sys.platform.startswith('win'):
                        # For Windows, use Adobe Reader to open in full screen
                        return subprocess.Popen(['start', 'AcroRd32.exe', '/A', 'page=1&zoom=100', file_path], shell=True)
                    elif sys.platform.startswith('darwin'):
                        # For macOS, open the PDF with Preview (no full screen option)
                        return subprocess.Popen(['open', file_path])
                    else:  # Assuming Linux
                        # Use a PDF viewer that supports full screen (e.g., Evince)
                        return subprocess.Popen(['evince', '--presentation', file_path])
                else:
                    # Attempt to read and print the content of non-PDF files
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                            content = file.read()  # Read the file content
                            print(content)  # Print the content to the console
                            return content  # Return the content
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")  # Print any error encountered


if __name__ == '__main__':
    # Prompt the user for the directory path
    directory = input("Enter the directory path: ")

    # Prompt the user whether to convert file names to integers
    convert_to_int_input = input("Convert file names to integers? (yes/no): ").strip().lower()
    convert_to_int = convert_to_int_input in ['yes', 'y', 'int']  # Convert input to boolean

    while True:
        # Prompt for file names (space-separated)
        file_names_input = input("Enter the file names (space-separated), or type 'exit' or 'quit' to stop: ")
        file_names = file_names_input.split()  # Split input into a list

        # Check if the user wants to exit the program
        if file_names_input.lower() in ["exit", "quit"]:
            print("Exiting the program.")
            break  # Exit the loop

        # Call the function with the user's arguments
        result = open_matching_files(directory, convert_to_int, *file_names)

        # Inform the user if no matching files were found
        if result is None:
            print(f"Cannot find the file '{file_names_input}' in this directory.")
