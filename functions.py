import os
import shutil

EXTENSION_MAP = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Archives': ['.zip', '.rar', '.tar.gz'],
}

def get_destination_folder(extension):
    for folder, ext in EXTENSION_MAP.items():
        if extension.lower() in ext:
            return folder
    return 'Others'


def organize_files(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            destination_folder = os.path.join(folder, get_destination_folder(ext))
            dest = os.path.join(destination_folder, filename)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(filepath, dest)