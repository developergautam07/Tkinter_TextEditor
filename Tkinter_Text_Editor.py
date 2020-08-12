''' Text Editor Mae using Python Tkinter '''

from tkinter import * # importing all modules from Tkinter
from tkinter import filedialog # importing filedialog module from Tkinter

def open_file():   # Function for opening a file
    try:
        t = filedialog.askopenfile(mode="r", title="Select File", filetype=[("All Files", "*.*")])
        content.insert(END, t.read())
    except:
        print("File Can't be Open")
    finally:
        if t:
            t.close()

def save():		# Funcion to save a file
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt") 
    if f is None:
        return
    try:
        text_user_in = str(content.get(1.0, END))
        f.write(text_user_in)
    except:
        print("This File Can't be Saved")    
    finally:
        f.close()
def exit_window():	# closing text editor
    window.destroy()

    
window = Tk()
window.title("Python Text Editor")  # Adding Title

main_menu = Menu(window)
window.config(menu=main_menu)

# Dropdown menu for File and Edit Tab
file_menu = Menu(main_menu)
edit_menu = Menu(main_menu)

# Adding File and Edit Tab
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)

# Adding Different Commands in File menu
file_menu.add_command(label="Open", command = open_file) # To Open a File
file_menu.add_command(label="New") # To Create a New File
file_menu.add_command(label="Save", command = save) # To Save a File
file_menu.add_command(label="Save As", command = save) # To Save a File
file_menu.add_separator() # Added a line as a Separator
file_menu.add_command(label="Exit", command = exit_window) # To Exit

# Adding Different Commands in Edit menu
edit_menu.add_command(label="Undo") # To Undo
edit_menu.add_command(label="Redo") # To Redo
file_menu.add_separator() # Added a line as a Separator
edit_menu.add_command(label="Copy") # To Copy Text
edit_menu.add_command(label="Paste") # To Paste Text

# Area For Writting
content = Text(window, width = 100) 
content.grid(row=0,column=0, padx=7, pady=7)

# Main Loop of the application
window.mainloop() 