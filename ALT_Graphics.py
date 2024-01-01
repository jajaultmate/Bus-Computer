import tkinter as tk

class GraphicsMenus:

    def __init__(self, main_frame, menu_frame):
        self.main_frame = main_frame
        self.menu_frame = menu_frame

    #Get back to main menu
    def show_main_screen(self):
        menu_frame.pack_forget()  #Hides menu screen
        main_frame.pack           #Shows main screen

    #Show menu with alternatives
    def show_menu(self):
        main.frame.pack_forget()  #Hides current screen
        menu.frame.pack()         #Shows menu screen

    #Show radio menu
    def open_radio(self, radio_frame):
        main.frame.pack_forget()   #Hides current screen
        radio.frame.pack()         #Show radio menu
