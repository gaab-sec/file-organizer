import os
from tkinter import filedialog
from functions import organize_files

if __name__ == "__main__":
    try: 
        # get user home folder as the default location
        home_path = os.path.expanduser('~')
        folder_path = filedialog.askdirectory(initialdir=home_path)

        organize_files(folder_path) 
        print(f"Files organized in: {folder_path}")

    except Exception as error: 
        # if some error happens, shows in terminal
        print(f"ERROR: {error}")