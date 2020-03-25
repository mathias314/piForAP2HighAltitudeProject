from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def getSenseData():
    sense_data = []
    
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())

    return sense_data

getSenseData()
print(getSenseData())


