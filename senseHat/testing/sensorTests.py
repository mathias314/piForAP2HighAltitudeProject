from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print("the pressure is: " + str(pressure) + "millibars")

temperature = sense.get_temperature()
print("the temperature is : " + str(temperature) + "c")

humidity = sense.get_humidity()
print("the humidity is: " + str(humidity))


