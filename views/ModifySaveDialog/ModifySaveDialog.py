import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from models.Save import *
from controllers.Controller import *

class ModifySaveDialog:
    
    def __init__(self, parentWindow, controller, save):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__controller = controller
        self.__save = save
        self.__parentWindow = parentWindow

        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/ModifySaveDialog/ModifySaveDialog.glade')
        self.__window = self.__builder.get_object("modifySaveWindow")
        self.__builder.get_object("saveNameLabel").set_text('" {} "'.format(save.getName()))

        self.__builder.get_object("nameEntry").set_text(save.getName())
        self.__builder.get_object("descriptionTextArea").get_buffer().set_text(save.getDescription())

        
        # Handles:
        self.__builder.get_object("cancelButton").connect("clicked", self.__cancelButtonHandle)
        self.__builder.get_object("confirmButton").connect("clicked", self.__confirmButtonHandle)
   

    def __cancelButtonHandle(self, arg):
        self.__window.destroy()
    
    def __confirmButtonHandle(self, args):
        name = self.__builder.get_object("nameEntry").get_text()
        buffer = self.__builder.get_object("descriptionTextArea").get_buffer()
        description = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
        progressBar = self.__builder.get_object("progressBar")
        progressBar.pulse()
        self.__controller.modifySave(self.__save, name,description)
        self.__parentWindow.refresh()
        self.__window.destroy()

    def run(self):
        self.__window.show_all()
