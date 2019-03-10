import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from models.PathMapper import *

from controllers.Controller import *

class SettingsDialog:
    
    def __init__(self, parentWindow, controller):
        self.__controller = controller
        self.__builder = Gtk.Builder()
        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/SettingsDialog/SettingsDialog.glade')
        self.__window = self.__builder.get_object("window")
        self.__path = self.__controller.getPathToSaves()

        self.__pathWidget = self.__builder.get_object('fileChooser')
        self.__pathWidget.set_current_folder(self.__path)        

        # Handles:
        self.__builder.get_object("cancelButton").connect("clicked",self.__cancelButtonHandle)
        self.__builder.get_object("confirmButton").connect("clicked",self.__confirmButtonHandle)
        self.__pathWidget.connect("current-folder-changed", lambda s: print("current: {}".format(self.__pathWidget.get_current_folder())))

    def run(self):
        self.__window.show_all()


    def __cancelButtonHandle(self,arg):
        self.__window.destroy()
        pass
    
    def __confirmButtonHandle(self,arg):
        path = self.__pathWidget.get_current_folder()
        pathMapper = PathMapper()
        pathMapper.setPath(path)
        self.__controller.setPathToSavesFromDatabase()
        self.__window.destroy()
        self.__parentWindow.refresh()
        pass
