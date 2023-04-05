# COMP593 - Lab 10 
from tkinter import * 
from tkinter import ttk
from pokeapi import fetch_poke_info
from image_lib import download_image, save_image_file, set_desktop_background_image, scale_image

class PokeImgViewer():
    """GUI Viewer for Pokemon Images"""
    def __init__(self, master):
        """
        Gui Initialization
        """
        self.root = master 
        self.root.configure(bg='#303f46')
        self.root.title('Poke_Viewer')
        self.root.iconbitmap("pokeball.ico")
        self.root.resizable(False, False)
    
    def imageFrame(self):
        """
        Initialize the image frame, define the widgets, place in root
        """
        
    def optionsFrame(self):
        """
        Initialize the options frame, define the widgets, place in root
        """


