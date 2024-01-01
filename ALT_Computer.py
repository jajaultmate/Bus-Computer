import tkinter as tk
from ALT_Buttons import Buttons
from ALT_Graphics import GraphicsMenus

#Main Application Window
root = tk.Tk()
root.title("SL Bus Computer")

#Set the window size
window_width = 1000
window_height = 600
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)
root.configure(bg="#23D1D5")

#Creating instance of "buttons" class to use here
buttons_functions = Buttons()
#Creating instance of "graphics_menus"
graphics_menus = GraphicsMenus(main_frame, menu_frame)

#FRAMES
main_frame = tk.Frame(root)
menu_frame = tk.Frame(root)
radio_frame = tk.Frame(root)


# Set the frames in the GraphicsMenus instance
#graphics_menus.main_frame = main_frame
#graphics_menus.menu_frame = menu_frame

#Label Widget
label = tk.Label(root, text="SL Bussdata")
label.pack()

#menu_label = tk.Label(menu_frame, text="Menu Screen")
#menu_label.pack()



#BUTTONS
menu_button = tk.Button(root, text="Meny",height=3, width=10, command=graphics_menus.show_menu)
menu_button.place(x=150, y=530)
#button1.pack()


radio_button = tk.Button(root, text="Radio",height=3, width=10, command=lambda: graphics_menus.open_radio(radio_frame))
radio_button.place(x=20, y=530)
#button2.pack()


#Main Event Loop
root.mainloop()

