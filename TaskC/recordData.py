import csv

class RecordData:
    def __init__(self):
        super().__init__()

    def writeTheRecord(self, winner,time):
        try:
            f = open('winner.csv', 'a') 
            dataNames = ['player', 'points', 'time']
            writer = csv.DictWriter(f, fieldnames=dataNames)
            writer.writerow({'player' : winner.getPlayerInfo().get("name"), 'points' : winner.getPlayerInfo().get("points"), 'time' : time})
        except FileNotFoundError:
            print("File doesnt exist")
        finally:
            f.close()