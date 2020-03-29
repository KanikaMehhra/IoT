import csv

class RecordData:
    def __init__(self):
        pass

    def recordData(self, data):
        try:
            f = open('winner.csv', 'a') 
            dataNames = ['player', 'points', 'time']
            writer = csv.DictWriter(f, fieldnames=dataNames)
            writer.writerow({'player' : data['player'], 'points' : data['points'], 'time' : data['time']})
        except FileNotFoundError:
            print("File doesnt exist")
        finally:
            f.close()

