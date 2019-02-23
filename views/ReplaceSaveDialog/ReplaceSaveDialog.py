import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from controllers.Controller import *

class ReplaceSaveDialog:
    
    def __init__(self, parentWindow):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()

        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/ReplaceSaveDialog/ReplaceSaveDialog.glade')
        self.__window = self.__builder.get_object("replaceSaveWindow")

        # Handles:
        self.__builder.get_object("noButton").connect("clicked",self.__noButtonHandle)
 

    def run(self):
        self.__window.show_all()


    def __noButtonHandle(self,arg):
        self.__window.destroy()
        pass
    
    def __yesButtonHandle(self,arg):
        pass