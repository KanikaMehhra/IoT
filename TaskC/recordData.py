import csv

class recordData:
    def __init__(self):
        super().__init__()
        self.__headers=["PlayerName", "WinningScore", "Time"]

    def writeTheRecord(self, winner,time):
        try:
            f = open('winner.csv', 'a') 
            writer = csv.writer(f)
            row=[]
            for key,value in winner.getPlayerInfo().items():
                row.append(value)
            row.append(time)
            writer.writerow(row)        
        except FileNotFoundError:
            print("File doesnt exist")
        finally:
            f.close()
            
