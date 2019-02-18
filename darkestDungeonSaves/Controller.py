class Controller:
    """ 
    Class proposed to controll mechanic of application
    """

    def __init__(self):
        
        self.__orderByOptions = [
            "Name",
            "Date ascending",
            "Date descending"
        ]

    def getOrderOptions(self):
        return self.__orderByOptions
    

    