from functions import *
from output import *


print("-------------------------------------")
print("[bold deep_sky_blue1]Weather Forecast App [/bold deep_sky_blue1]")
cityName = input("Enter the City Name: ")

data = findCity(cityName)
printOutput(cityName, data)

