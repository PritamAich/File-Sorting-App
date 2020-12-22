import os
import shutil

import tkinter
from tkinter  import *
from tkinter import filedialog
import tkinter.font as tkFont

from PIL import ImageTk, Image


def file_sort(main_dir):


    # Getting all the files inside the folder
    files_list = [f for f in os.listdir(main_dir) if os.path.isfile(os.path.join(main_dir, f))]

    # Corner case:
    # If no files are there inside the folder
    # Print an error message and return.
    # Else continue the process
    if not files_list:
        return False
        
    """
    1. Take each file from the list, and split the file name from its extension
    2. Create a folder with the extension name
    3. Cut and paste each file of that particular extension
       inside those extension folders. 
    """    
    for file in files_list:
        extension = file.split(".")
        
        extension_folder = os.path.join(main_dir, extension[1].upper())

        try: 
            os.makedirs(extension_folder, exist_ok = True) 
             
        except OSError as error: 
            print("Directory can not be created.") 

        # The shutil module is used for file operations
        # like copy, move, delete
        # Parameters: source path, destination path
        shutil.move(os.path.join(main_dir, file), os.path.join(main_dir, extension_folder, file)) 
    
    return True


if __name__ == '__main__':
    
    # Will use Tkinter GUI for accepting folder / directory path
    window = Tk()

    window.title("File Sorting App") #Window title
    window.geometry("750x400") #Height and width of window
    icon_image = ImageTk.PhotoImage(Image.open('icon.ico')) #Window favicon
    window.iconphoto(False, icon_image)

    # Setting font style
    font_l1 = tkFont.Font(size = 14)
    font_l2 = tkFont.Font(size = 12)

    label_1 = Label(window, text = 'Hello! Welcome to the File sorting Application!', font = font_l1, foreground = "#048a04").grid(row = 0, pady = 30, padx = 100)

    label_2 = Label(window, text = 'Enter the folder / directory path inside which the files need to be sorted.',font = font_l2).grid(row = 1, pady = 20)

    # Entry is used to take user input.
    # Here the folder path will be taken 
    file_path_entry = Entry(window, width = 80)
    file_path_entry.grid(row = 2, column = 0, padx = 70)
    
    def sort_files(main_dir):

        # Calling the main sorting function
        files_sorted = file_sort(main_dir)

        font_confirm_label = tkFont.Font(size = 12)
        # Checking if sorting condition
        # condintion will go to else if there is no files in the folder
        if files_sorted:
            confirm_label = Label(window, text = "Files sorted successfully!", foreground = "blue", font = font_confirm_label).grid(row = 4, pady = 30)

        else:
            confirm_label = Label(window, text = "Directory / folder does not have any file.", foreground = 'red', font = font_confirm_label).grid(row = 4, pady = 30)

    # Function where the user have to select the folder path
    def browsefunc():

        folder_path = filedialog.askdirectory()
        file_path_entry.insert(tkinter.END, folder_path)

        main_dir = file_path_entry.get()

        # The main button on clicking which the sorting will be done
        sort_button = Button(text = "Sort Files", width = 20, command = lambda: sort_files(main_dir))
        sort_button.grid(row = 3, column = 0, pady = 20)
        
    # Button to browse to the specified folder path
    browse_button = Button(text = "Browse", width = 10, command = browsefunc)
    browse_button.grid(row = 2, column = 1)


    window.mainloop()