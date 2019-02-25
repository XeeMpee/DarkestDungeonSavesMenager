import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import re

from controllers.Controller import *

class NewSaveDialog:

    def __init__(self,profileNumber):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__profileNumber = profileNumber

        self.__builder.add_from_file('views/NewSaveDialog/NewSaveDialog.glade')
        self.__window = self.__builder.get_object("newSaveWindow")

        # Handles:
        self.__builder.get_object("cancelButton").connect("clicked", self.__cancelButtonHandle)
        self.__builder.get_object("confirmButton").connect("clicked", self.__confirmButtonHandle)
   
    def run(self):
        self.__window.show_all()


    def __cancelButtonHandle(self, arg):
        self.__window.destroy()
    
    def __confirmButtonHandle(self, args):
        name = self.__builder.get_object("nameEntry").get_text()
        buffer = self.__builder.get_object("descriptionTextArea").get_buffer()
        description = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        progressBar = self.__builder.get_object("progressBar")
        print(progressBar)
        progressBar.pulse()
        self.__controller.saveGame(name,description,self.__profileNumber)
        self.__window.destroy()