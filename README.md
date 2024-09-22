# File Opener Script

A Python script to open specific files in a given directory based on user-defined file names. It supports opening PDF files in full screen and reading the content of text files. The script can also convert file names to integers if specified.

## Features

- Opens PDF files in full screen mode using the default PDF viewer based on the operating system.
- Reads and prints the content of text files.
- Supports optional conversion of file names to integers for matching.

## Requirements

- Python 3.x
- Standard libraries: `os`, `re`, `subprocess`, `sys`

## Usage

1. **Clone the repository or download the script.**
2. **Open a terminal and navigate to the script's directory.**
3. **Run the script:**

   ```bash
   python finder-x.py
   ```
   
## Follow the prompts
Enter the directory path where the files are located.
Specify whether to convert file names to integers (yes/no).
Enter the file names you want to match (space-separated), or type exit or quit to stop the program.


## Notes
- Windows: The script uses Adobe Reader to open PDF files. Ensure Adobe Reader is installed and available in your system PATH.
- macOS: The script uses Preview to open PDF files. Note that full screen mode cannot be enforced via the command line.
- Linux: The script defaults to using Evince. You may replace it with your preferred PDF viewer that supports full screen.
