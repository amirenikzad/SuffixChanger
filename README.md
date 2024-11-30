# File Suffix Changer

A simple Python script to rename files in a directory by changing their suffix. This script is useful for batch-renaming files with specific extensions.

## Features
- Automatically scans a specified directory for files with a specific suffix.
- Renames files by replacing the old suffix with a new one.
- Prints logs of all renamed files.

## Requirements
- Python 3.6 or higher.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FileSuffixChanger.git
   cd FileSuffixChanger
   ```

2. Edit the script:
   Open the `suffix_changer.py` file and set the `directory_path` to the full path of the directory containing the files you want to rename.  
   Example:
   ```python
   directory_path = r"E:\22\content"
   ```

3. Run the script:
   Execute the script using Python:
   ```bash
   python suffix_changer.py
   ```

4. View the output:
   The script logs renamed files to the console:
   ```plaintext
   Renamed: E:\22\content\example.change_suffix_later -> E:\22\content\example.mp4
   ```

## Customization
You can customize the suffixes to suit your needs:
- Replace `.change_suffix_later` with the suffix you want to replace.
- Replace `.mp4` with your desired new suffix.

For example:
```python
change_file_suffix(directory_path, ".txt", ".pdf")
```

## Code Example

```python
import os

def change_file_suffix(directory, old_suffix, new_suffix):
    for filename in os.listdir(directory):
        if filename.endswith(old_suffix):
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, filename.replace(old_suffix, new_suffix))
            
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

directory_path = r"yourpath"
change_file_suffix(directory_path, ".change_suffix_later", ".mp4")
```

## Notes
- Ensure the directory path is correct and contains files to rename.
- It's recommended to back up your files before running the script.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
