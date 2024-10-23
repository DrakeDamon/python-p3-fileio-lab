from pathlib import Path

def write_file(file_name, file_content):
    # Create the file path using pathlib's with_suffix to add the .txt extension
    file_path = file_name.with_suffix(".txt")
    
    # Open and write to the file
    with open(file_path, mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)


def append_file(file_name, append_content):
    file_path = file_name.with_suffix(".txt")

    with open(file_path, mode='a', encoding='utf-8') as text_file:
        text_file.write(append_content)

def read_file(file_name):
    file_path = file_name.with_suffix(".txt")

    # Use 'with' to automatically close the file after reading
    with open(file_path, encoding='utf-8') as text_file:
        content = text_file.read()
    
    return content  # Return the content for further use