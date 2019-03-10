import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango   
import re

from controllers.Controller import *

class NewSaveDialog:

    def __init__(self,parentWindow,profileNumber):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__profileNumber = profileNumber
        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/NewSaveDialog/NewSaveDialog.glade')
        self.__window = self.__builder.get_object("newSaveWindow")
        self.__builder.get_object("descriptionTextArea").set_wrap_mode(Pango.WrapMode.WORD_CHAR)

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
        self.__parentWindow.refresh()