import requests
import json

########################################
### RAW DATA ###########################
########################################

# Sources

current_url = "https://api.weather.gov/gridpoints/PSR/175,50"
current_test_path = r"test_data_current.json"

payload = ""
headers = ""

# Define raw data object
class RawData:
  def __init__(self, url, test_path):
    self.url = url
    self.test_path = test_path

  def get_data(self):   # Creates pyDict dictionary from test_path JSON
    if self.url is None:
      self.jsonData = open(self.test_path, "r") # Opens JSON in read mode
      self.rawData = self.jsonData.read() # Stores JSON into rawData
      self.pyDict = json.loads(self.rawData) # Converts rawData into dictionary

    elif self.test_path is None:  # Creates pyDict dictionary from API url
      self.response = requests.request("GET", self.url, data = payload, headers = headers)  # Opens JSON from url
      self.rawData = self.response.text # Stores JSON into rawData
      self.pyDict = json.loads(self.rawData) # Converts rawData into dictionary

# Create objects
current_data = RawData(None, current_test_path)   # Test data
#current_data = RawData(current_url, None)        # Real data

# Do the import
current_data.get_data()

########################################
### CLEAN DATA #########################
########################################

# Define general value object

class DataContainer:

  def __init__(self, value1):
    self.value1 = value1

  def convertSkyCond(self):
    if self.value1 < 25:
      return "Clear"
    elif self.value1 >= 25 and self.value1 < 50:
      return "Partly Cloudy"
    elif self.value1 >= 50 and self.value1 < 75:
      return "Mostly Cloudy"
    elif self.value1 >= 75:
      return "Overcast"

  def returnCoordAsStr(self):
    return str(round(self.value1 , 2))

  def returnCTempAsFStr(self):
    return str(round((self.value1 * 9/5 + 32)))

  def returnCTempAsFInt(self):
    self.convertToF()
    self.round()

# Assign values to objects

def reload():
  global latCurrent, longCurrent, skyCond, currentTemp, highTemp, lowTemp, feelsLike, humidity, windDirection, windSpeed, windGust
  latCurrent = DataContainer(current_data.pyDict["geometry"]["coordinates"][0][0][1])
  longCurrent = DataContainer(current_data.pyDict["geometry"]["coordinates"][0][0][0])
  skyCond = DataContainer(current_data.pyDict["properties"]["skyCover"]["values"][0]["value"])    
  currentTemp = DataContainer(current_data.pyDict["properties"]["temperature"]["values"][0]["value"])
  highTemp = DataContainer(current_data.pyDict["properties"]["maxTemperature"]["values"][0]["value"])
  lowTemp = DataContainer(current_data.pyDict["properties"]["minTemperature"]["values"][0]["value"])
  feelsLike = DataContainer(current_data.pyDict["properties"]["apparentTemperature"]["values"][0]["value"])
  humidity = DataContainer(current_data.pyDict["properties"]["relativeHumidity"]["values"][0]["value"])
  windDirection = DataContainer(current_data.pyDict["properties"]["windDirection"]["values"][0]["value"])
  windSpeed = DataContainer(current_data.pyDict["properties"]["windSpeed"]["values"][0]["value"])
  windGust = DataContainer(current_data.pyDict["properties"]["windGust"]["values"][0]["value"])

reload() # RELOAD THE DATA