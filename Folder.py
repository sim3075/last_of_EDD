class Folder:
    def __init__(self, name:str):
        self.name = name
        self.l_child = None
        self.l_central_child = None
        self.r_central_child = None
        self.r_child = None
        self.elements = 0

    def modify_name(self, new_name):
        self.name = new_name