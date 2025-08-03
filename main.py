import os
from tkinter import filedialog
from functions import organize_files

if __name__ == "__main__":
    try:
        home_path = os.path.expanduser('~')
        folder_path = filedialog.askdirectory(initialdir=home_path)
        organize_files(folder_path)
        print(f"Arquivos organizados em: {folder_path}")

    except Exception as error:
        print(f"ERROR:{error}")