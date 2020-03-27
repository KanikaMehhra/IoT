import json
class DataInput:
    def __init__(self, path):
        f = open(path,) 
        self.__data = json.load(f)
        f.close()

    def getData(self):
        return self.__data