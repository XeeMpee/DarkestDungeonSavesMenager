import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from models.Save import *
from controllers.Controller import *

class DeleteSaveDialog:
    
    def __init__(self, parentWindow, controller, save):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__controller = controller
        self.__save = save
        self.__parentWindow = parentWindow

        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/DeleteSaveDialog/DeleteSaveDialog.glade')
        self.__window = self.__builder.get_object("deleteSaveWindow")
        self.__builder.get_object("saveNameLabel").set_text('" {} "'.format(save.getName()))

        # Handles:
        self.__builder.get_object("noButton").connect("clicked",self.__noButtonHandle)
        self.__builder.get_object("yesButton").connect("clicked", self.__yesButtonHandle)
        self.__window.connect("key-press-event",self.on_key_press_event)

    def run(self):
        self.__window.show_all()


    def __noButtonHandle(self,arg):
        self.__window.destroy()
        pass
    
    def __yesButtonHandle(self,arg):
        self.__controller.deleteSave(self.__save)
        self.__parentWindow.refresh()
        self.__window.destroy()

    def on_key_press_event(self, widget, event):
        if event.keyval == 65307:
            self.__noButtonHandle(None)
        if event.keyval == 65293:
            self.__yesButtonHandle(None)