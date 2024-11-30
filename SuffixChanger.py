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
