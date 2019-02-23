import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf
import re

from controllers.Controller import *
from views.NewSaveDialog.NewSaveDialog import *

class MainWindow():
    """ 
    Main window class
    """

    def __init__(self):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__window = Gtk.Window()

        self.__saveBoxRowSize = (0,80)

    def run(self):
        self.__builder.add_from_file("./views/MainWindow/MainWindow.glade")
        self.__window = self.__builder.get_object("window")
        
        self.__window.set_title('DarkestDungeonSaveMenager')
        self.__fillProfilesComboBox()
        self.__fillOrderByComboBox()
        self.__fillSavesArea()

        self.__builder.get_object('actionNameLabel').set_text('Ready')
        self.__builder.get_object('actionName').set_text('Done')
        self.__window.connect('destroy', Gtk.main_quit)

        self.__builder.get_object('saveGameButton').connect("clicked",self.__saveGame)

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("views/MainWindow/MainWindow.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.__window.show_all()

        Gtk.main()


    def __fillOrderByComboBox(self):
        comboBox = self.__builder.get_object('sortByComboBox')
        for i in self.__controller.getOrderOptions():
            comboBox.append_text(i[0])
        comboBox.set_active(2)



    def __fillProfilesComboBox(self):
        comboBox = self.__builder.get_object('profilesCombo')
        for i in self.__controller.getProfilesList():
            profileNumber = re.findall('[0-9]+',i[0])[0]
            comboBox.append_text("Profile " + profileNumber + ": " + i[1])
        comboBox.set_active(0)

    def __fillSavesArea(self):
        self.__newSaveRow = Gtk.ListBoxRow(name="saveRow")
        self.__builder.get_object('savesListBox').add(self.__newSaveRow)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        newSaveIcon = Gtk.Image()
        newSaveIcon.set_from_file('images/newSave.png')
        hbox.pack_start(newSaveIcon, False, True, 20)
        hbox.pack_start(Gtk.Label('New save...'), False, True, 0)
        hbox.set_size_request(self.__saveBoxRowSize[0], self.__saveBoxRowSize[1])
        self.__newSaveRow.add(hbox)

        saveMapper = SaveMapper()
        saves = saveMapper.getAllSaves()
        
        for i in saves:
            self.__builder.get_object('savesListBox').add(self.__createSaveRow(i))

   
    def __createSaveRow(self, i):
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            saveIcon = Gtk.Image()
            saveIcon.set_from_file('images/save.png')
            hbox.pack_start(saveIcon, False, True, 20)
            hbox.pack_start(Gtk.Label(i.getName()), False, True, 0)
            timebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=50)
            
            hbox.pack_end(timebox, False, False, 0)
            timebox.set_margin_top(20)
            timebox.set_margin_right(20)
            timebox.set_margin_left(20)
            datetime = "{}\n{}".format(i.getDate(), i.getTime())
            timebox.pack_start(Gtk.Label(datetime), False, True, 0)

            optionBox = Gtk.Box(Gtk.Orientation.HORIZONTAL, spacing=0)
          
            loadIcon = Gtk.Image()
            loadIcon.set_from_file('images/load.png')
            loadButton = Gtk.Button()
            loadButton.set_image(loadIcon)
            loadButton.set_size_request(30,30)
            
            deleteButton = Gtk.Button()
            deleteIcon = Gtk.Image()
            deleteIcon.set_from_file('images/delete.png')
            deleteButton.set_image(deleteIcon)

            modifyIcon = Gtk.Image()
            modifyIcon.set_from_file('images/load.png')
            modifyButton = Gtk.Button()
            modifyButton.set_image(modifyIcon)
            
            optionBox.pack_start(loadButton,False,False,0)
            optionBox.pack_start(deleteButton,False,False,0)
            hbox.pack_end(optionBox,False,False,0)

            hbox.set_size_request(self.__saveBoxRowSize[0], self.__saveBoxRowSize[1])
            row.add(hbox)
            return row
 
 
    def __saveGame(self, arg):
        if(self.__newSaveRow.is_selected()):
            dialog = NewSaveDialog()
            dialog.run()
        else:
            print('nooo')
 