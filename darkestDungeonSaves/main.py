from MainWindow import *
from Controller import *

if __name__ == "__main__":

    controller = Controller()
    controller.generateProfilesList()
    
    mainWindow = MainWindow()
    mainWindow.run()
    pass