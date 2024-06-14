---

# Directory Organizer

This script organizes files in a specified directory into subdirectories based on their file extensions. Files without extensions are moved to a folder named "Other".

## Features

- Organizes files by their extensions into respective folders.
- Creates new directories for each file type if they don't already exist.
- Moves files to their respective directories.

## Requirements

- Python 3.x
- `os` and `shutil` libraries (which are included in the Python standard library)

## Usage

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/gautamraj8044/fileorganiser
   cd fileorganiser
   ```

2. **Modify the script to set your target directory**:
   - Open the script and change the `path` variable in the `main` function to the directory you want to organize. For example:
     ```python
     path = r"C:/Users/YourUsername/Downloads/"
     ```

3. **Run the script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```bash
     python fileorganiser.py
     ```


### fileorganiser(path)

This function:
- Iterates through all files in the specified directory.
- Skips directories and processes only files.
- Extracts the file extension and creates a corresponding subdirectory.
- Moves the file to the appropriate subdirectory.

### main()

This function:
- Sets the directory path to be organized.
- Calls `organiseDire` to organize the files in the specified directory.


## Notes

- Ensure the specified directory path is correct.
- The script copies files to the new directories. If you want to move files instead of copying, replace `shutil.copyfile` with `shutil.move`.
