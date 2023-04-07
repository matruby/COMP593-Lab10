# COMP593 - Lab 10 
from tkinter import * 
from PIL import ImageTk, Image 
from tkinter import ttk 
import ctypes 
import os 
from pokeapi import get_pokemon_names, download_pokemon_artwork

class PokeImgViewer():
    """GUI Viewer for Pokemon Images"""
    def __init__(self, master):
        """
        Gui Initialization
        """
        # The Tk() object is passed in as 'master'
        self.root = master 
        # Set the minimum window size 
        self.root.minsize(600, 700)
        # Configure the background colour of the window 
        self.root.configure(bg='#56717D')
        # Allow window scaling 
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        # Set the window title and window favicon 
        self.root.title('Poke_Viewer')
        self.root.iconbitmap("pokeball.ico")
        # Attempt to allow the program to have a taskbar image  
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
        # Class variables for the script 
        self.script_path = os.path.abspath(__file__)
        self.script_dir = os.path.dirname(self.script_path)
        self.image_cache_dir = os.path.join(self.script_dir, 'images')
        
    def main_window(self):
        """
        Initialize the image frame, define the widgets, place in root
        """
        # Initialize the frame widget and place it in the 
        self.image_frame = Frame(self.root, bg='#56717D')
        self.image_frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        # Configure the weight so it can resize 
        self.image_frame.columnconfigure(0, weight=1)
        self.image_frame.rowconfigure(0, weight=75)
        
        # Initialize the image and label widget, and assign the image to the label
        self.poke_img = PhotoImage(file=os.path.join(self.script_dir, 'pokemon_logo.png'))
        self.lbl_poke_image = Label(self.image_frame, image=self.poke_img, bg='#4D646F')
        self.lbl_poke_image.grid(row=0, column=0)

        # Get the list of all Pokemon names 
        pokemon_name_list = get_pokemon_names()
        
        # Create the combobox widget, set the default option 
        self.cbox_poke_names = ttk.Combobox(self.image_frame, value=pokemon_name_list, state='readonly')
        self.cbox_poke_names.set('Select a Pokemon')
        self.cbox_poke_names.grid(row=1, column=0, padx=10, pady=10)

        # When the option for the combobox has changed use the handler method 
        self.cbox_poke_names.bind('<<ComboboxSelected>>', self.handle_pokemon_sel)  
        
        # Initialize and place the set desktop background button 
        self.btn_set_desktop = ttk.Button(self.image_frame, text='Set as Desktop Image', state=DISABLED, command=self.handle_set_desk)
        self.btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)
        

    def handle_pokemon_sel(self, event):
        """
        Changes the Pokemon image if the combo box option is changed 
        """
        # Change the state of the set desktop button to allow wallpaper changes  
        self.btn_set_desktop['state'] = NORMAL

        # Make the image cache directory if it doesn't exist
        if not os.path.isdir(self.image_cache_dir):
            os.mkdir(self.image_cache_dir)

        # Download and save the artwork for the selected Pokemon
        pokemon_name = self.cbox_poke_names.get()
        self.image_path = download_pokemon_artwork(pokemon_name, self.image_cache_dir)

        # Display the Pokemon Artwork 
        if self.image_path is not None:
            self.poke_img['file'] = self.image_path

    def handle_set_desk(self):
        """
        Set's the desktop background for to the current image 
        """
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, self.image_path, 0)
        except Exception:
            print('Setting Background Failed!!')
        

if __name__ == '__main__':
    # Initialize root  
    root = Tk()
    # Run the class 
    poke_gui = PokeImgViewer(root)
    
    # Add the frames 
    poke_gui.main_window()

    # Run the event loop 
    root.mainloop()


