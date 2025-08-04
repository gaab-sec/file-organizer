import os
import shutil

# map of file type and their extension 
EXTENSION_MAP = { # example only —> editable
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Archives': ['.zip', '.rar', '.tar.gz'],
}

def get_destination_folder(extension):
    # check which folder matches the file extension
    for folder, ext in EXTENSION_MAP.items():
        if extension.lower() in ext:
            return folder
    return 'Others' # if dont match anyone, send to 'Others'


def organize_files(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            
            # sets the destination folder based on the extension
            dest_folder = os.path.join(folder, get_destination_folder(ext))
            dest = os.path.join(dest_folder, filename)

            os.makedirs(
                dest_folder, 
                exist_ok=True # dont raise exception if the folder already exists
            )
            shutil.move(filepath, dest)
