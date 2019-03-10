import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

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
        self.__builder.get_object("descriptionTextArea").set_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.__window.connect("key-press-event",self.on_key_press_event)
        
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

    def on_key_press_event(self, widget, event):
        if event.keyval == 65307:
            self.__cancelButtonHandle(None)
        if event.keyval == 65293:
            self.__confirmButtonHandle(None)

    def run(self):
        self.__window.show_all()

    
