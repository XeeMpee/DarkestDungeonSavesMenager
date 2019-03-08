import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf
import re

from controllers.Controller import *
from controllers.OrderEnum import *
from views.NewSaveDialog.NewSaveDialog import *
from views.ReplaceSaveDialog.ReplaceSaveDialog import *
from views.DeleteSaveDialog.DeleteSaveDialog import *
from views.UploadSaveDialog.UploadSaveDialog import *
from views.ModifySaveDialog.ModifySaveDialog import *

class MainWindow():
    """ 
    Main window class
    """

    def __init__(self):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__window = Gtk.Window()

        self.__saveBoxRowSize = (0,80)

        self.__savesList = list()

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

        self.__builder.get_object('saveGameButton').connect("clicked",self.__saveGameHandle)
        self.__builder.get_object('refreshButton').connect("clicked",self.refresh)
        self.__builder.get_object('sortByComboBox').connect("changed",self.refresh)

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

    def __fillSavesArea(self, order=OrderEnum.TIMEDESC):
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
        saves = saveMapper.getAllSaves(order)
        
        for i in saves:
            self.__builder.get_object('savesListBox').add(self.__createSaveRow(i))

   
    def __createSaveRow(self, i):
            row = Gtk.ListBoxRow()
            row.set_tooltip_text(i.getDescription())
            # row.set_property('has_tooltip', True)
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            saveIcon = Gtk.Image()
            saveIcon.set_from_file('images/save.png')
            hbox.pack_start(saveIcon, False, True, 20)
            # hbox.pack_start(Gtk.Label(i.getId()), False, False, 0)
            hbox.pack_start(Gtk.Label(i.getName(), name="saveLabel"), False, True, 0)
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
            loadButton.connect("clicked", self.__uploadButtonClicked,i)
            
            deleteButton = Gtk.Button()
            deleteIcon = Gtk.Image()
            deleteIcon.set_from_file('images/delete.png')
            deleteButton.set_image(deleteIcon)
            deleteButton.connect("clicked",self.__deleteButtonClicked,i)

            modifyIcon = Gtk.Image()
            modifyIcon.set_from_file('images/modify.png')
            modifyButton = Gtk.Button()
            modifyButton.set_image(modifyIcon)
            modifyButton.connect("clicked",self.__modifyButtonClicked,i)
            
            optionBox.pack_start(loadButton,False,False,0)
            optionBox.pack_start(modifyButton,False,False,0)
            optionBox.pack_start(deleteButton,False,False,0)
            hbox.pack_end(optionBox,False,False,0)

            hbox.set_size_request(self.__saveBoxRowSize[0], self.__saveBoxRowSize[1])
            row.add(hbox)
            
            self.__savesList.append((row,i))
            return row
 
 
    def __clearSaveListBox(self):
        savesListBox = self.__builder.get_object("savesListBox")
        saves = savesListBox.get_children()
        for i in saves:
            savesListBox.remove(i)
    
    
    def refresh(self, order=OrderEnum.TIMEDESC):    
        self.__clearSaveListBox()
        orderByOption = self.__builder.get_object("sortByComboBox").get_active()
        enum = (OrderEnum)(orderByOption)
        self.__fillSavesArea(enum)
        self.__window.show_all()
        

    def __saveGameHandle(self, arg):
        if(self.__newSaveRow.is_selected()):
            
            profileNumber = self.__builder.get_object("profilesCombo").get_active()        
            dialog = NewSaveDialog(self,profileNumber)
            dialog.run()
        elif(len(self.__builder.get_object("savesListBox").get_selected_rows()) > 0):
            
            profileNumber = self.__builder.get_object("profilesCombo").get_active()  
            save = self.__getSaveFromSelectedRow()
            dialog = ReplaceSaveDialog(self, self.__controller, save, profileNumber)
            dialog.run()
        

    def  __deleteButtonClicked(self, widget, save):
        dialog = DeleteSaveDialog(self, self.__controller,save)
        dialog.run()

    def __uploadButtonClicked(self,widget,save):
        profileNumber = self.__builder.get_object("profilesCombo").get_active()
        dialog = UploadSaveDialog(self, self.__controller,save,profileNumber)
        dialog.run()


    def __modifyButtonClicked(self,widget,save):
        dialog = ModifySaveDialog(self,self.__controller,save)
        dialog.run()

 
    def __getSaveFromSelectedRow(self) -> Save:
        savesListBox = self.__builder.get_object("savesListBox")
        actualRow  = savesListBox.get_selected_rows()[0]
        
        for (row,save) in self.__savesList:
            if(actualRow == row):
                return save
