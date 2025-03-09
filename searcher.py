import json

def get_current_data():
  global rawDataCurrent
  jsonDataCurrent = open(r"C:\Users\jnast\Desktop\python projects\test_data_current.json", "r") # Opens json in read mode
  rawDataCurrent = jsonDataCurrent.read() # Stores JSON into rawDataCurrent

########################################

get_current_data()
pyDictCurrent = json.loads(rawDataCurrent) # Converts rawDataCurrent into dictionary

#print(list(pyDictCurrent["properties"]["apparentTemperature"]["values"][0]["value"]))
print(pyDictCurrent["properties"]["windGust"]["values"][0]["value"])