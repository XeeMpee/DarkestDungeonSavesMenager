import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import re

from controllers.Controller import *

class MainWindow():
    """ 
    Main window class
    """

    def __init__(self):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__window = Gtk.Window()

    def run(self):
        self.__builder.add_from_file("./views/MainWindow.glade")
        self.__window = self.__builder.get_object("window")
        
        self.__window.set_title('DarkestDungeonSaveMenager')
        self.__fillProfilesComboBox()
        self.__fillOrderByComboBox()
        self.__builder.get_object('actionNameLabel').set_text('Ready')
        self.__builder.get_object('actionName').set_text('Done')
        self.__window.connect('destroy', Gtk.main_quit)
        self.__window.show_all()

        Gtk.main()

er.getProfilesList():
            comboBox.append_text(i[0] + ": " + i[1])
        comboBox.append_te
    def __fillOrderByComboBox(self):
        comboBox = self.__builder.get_object('sortByComboBox')
        for i in self.__controller.getOrderOptions():
            comboBox.append_text(i)
        comboBox.set_active(2)


    def __fillProfilesComboBox(self):
        comboBox = self.__builder.get_object('profilesCombo')
        for i in self.__controller.getProfilesList():
            profileNumber = re.findall('[0-9]+',i[0])[0]
            comboBox.append_text("Profile " + profileNumber + ": " + i[1])
        comboBox.set_active(0)