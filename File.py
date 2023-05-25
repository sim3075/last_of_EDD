class File:
    def __init__(self, name, extension, weight):
        self.name = name
        self.extension = extension
        self.weight = weight
        

    def modify_name(self, new_name):
        self.name = new_name
    
    def modify_extension(self, new_extension):
        self.extension = new_extension

    def modify_weight(self, new_weight):
        self.weight = new_weight
    
    def filename(self):
        return self.name + "." + self.extension + " " + self.weight