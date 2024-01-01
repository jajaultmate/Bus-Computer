'''
#Function for the button1 when it is clicked
def menu(menubutton):
    menubutton.config(text="Avbryt")

def radio(radiobutton):
    radiobutton.config(text="Avbryt")
'''

#Class to define actions of buttons
class Buttons:

    def gotomenu(self, menu):
        menu.config(text="Tillbaks")


    def gotoradio(self, radio):
        radio.config(text="Avbryt")