import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow():
    """ 
    Main window class
    """

    def __init__(self):
        self.__builder = Gtk.Builder()
        self.__window = Gtk.Window()

    def run(self):
        self.__builder.add_from_file("./darkestDungeonSaves/MainWindow.glade")
        self.__window = self.__builder.get_object("window")

        self.__window.set_title('DarkestDungeonSaveMenager')

        self.__window.connect('destroy', Gtk.main_quit)
        self.__window.show_all()

        Gtk.main()