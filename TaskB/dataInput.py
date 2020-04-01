import json
class DataInput:
    def __init__(self, path):
        f = open(path, 'r') 
        self.__data = json.load(f)
        f.close()

    def getData(self):
        return self.__data