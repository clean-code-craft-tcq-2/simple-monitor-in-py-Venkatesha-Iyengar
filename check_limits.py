from abc import ABC, abstractmethod

#Dictionary to define messages in different languages
#The messages are in a list, [English, German, Spanish] -> Can be scaled to any number of languages
Output_Messages = {
  "Low_Breach" : ["LOW BREACH", "NIEDRIGE VERLETZUNG", "INCUMPLIMIENTO BAJO"],
  "High_Breach" : ["HIGH BREACH", "HOHE VERLETZUNG", "ALTO INCUMPLIMIENTO"],
  "Normal" : ["NORMAL", "NORMAL", "NORMAL"],
  "Low_Warning" : ["LOW WARNING", "NIEDRIGE WARNUNG", "ADVERTENCIA BAJA"],
  "High_Warning" : ["HIGH WARNING", "HOHE WARNUNG", "ADVERTENCIA ALTA"]
  }

#Dictionary for market parameters
Market_Parameters = {
  "Language" : {
    "English" : 0,
    "German" : 1,
    "Spanish" : 2
    },

  #Future Scope -> For Extension 3
  "Temperature_Sensor_Type":{
    "Fahrenhiet" : "F",
    "Celcius" : "C",
    "Kelvin" : "K"
    }
  }

#Create an abstract method for battery OK Check, so any new way of checking can be implemented 
class abstraction(ABC):
    @abstractmethod
    def Battery_OK_Check(self):
        pass

#High Level Module for BMS
class Battery_Management_System():
  
  def __init__(self, min_value, max_value, tolerance, m:abstraction):
    self.minimum_value = min_value
    self.maximum_value = max_value
    self.warning_min = min_value + ((tolerance*max_value)/100)
    self.warning_max = max_value - ((tolerance*max_value)/100)
    self.market_type = m

  def Battery_Status_Check(self, value):
    return_message, status = self.market_type.Battery_OK_Check(value, self)
    print(return_message)
    return status


#Function to test if value in Range
def check_breach(value,BMS_Object):
  if value < BMS_Object.minimum_value:
    return "Low_Breach"

  elif value > BMS_Object.maximum_value:
    return "High_Breach"

  else:
      return "Normal"

def check_warning(value,BMS_Object):
    if value < BMS_Object.warning_min:
      return "Low_Warning"
    elif value > BMS_Object.warning_max:
      return "High_Warning"
    else:
      return "Normal"

def value_in_range(value, BMS_Object, warning_Flag):
  return_status = "Normal"
  return_status = check_breach(value, BMS_Object)
  if warning_Flag == True and return_status == "Normal":
      return_status = check_warning(value, BMS_Object)

  print(return_status)
  return return_status
      

#Pure Functions to convert between different units
def convert_farenheit_to_celcius(farenheit):
    return ((farenheit - 32) * 5 / 9)

def convert_celcius_to_farenheit(celcius):
    return ((celcius + 32) * 9 / 5)

     
#This is the low-level module, can be changed in future if customer expects a new way of checking for particular Market
class Battery_Validator_Indian_Market(abstraction):
  
  def __init__(self, language, warning_flag, temp_market_display):
    self.Language = language
    self.warning_flag = warning_flag
    self.temp_market_display = temp_market_display

  def Battery_OK_Check(self, Value_to_Test, BMS_Object):
    status_check = value_in_range(Value_to_Test, BMS_Object, self.warning_flag)
    print(status_check)
    return f"Status Message: {Output_Messages[status_check][int(Market_Parameters['Language'][self.Language])]}", status_check

#This is the low-level module, can be changed in future if customer expects a new way of checking for particular Market
class Battery_Validator_German_Market(abstraction):

  def __init__(self, language, warning_flag, temp_market_display):
    self.Language = language
    self.warning_flag = warning_flag
    self.temp_market_display = temp_market_display
  
  def Battery_OK_Check(self, Value_to_Test, BMS_Object):
    status_check = value_in_range(Value_to_Test, BMS_Object, self.warning_flag)
    return f"Status Message: {Output_Messages[status_check][int(Market_Parameters['Language'][self.Language])]}", status_check
