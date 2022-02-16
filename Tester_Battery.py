from check_limits import *

#Tester which is encapsulated instead of using multiple asserts
class Test_Battery_OK():
  
  def Tester(self, BMS_Object, Value_to_Test, expected_result):
    assert(BMS_Object.Battery_Status_Check(Value_to_Test) == expected_result)
    

if __name__ == '__main__':
  #Object Initialization Market Specific
  Object_Indian_Market = Battery_Validator_Indian_Market(language="English", warning_flag=True, temp_market_display= "Celcius")
  Object_German_Market = Battery_Validator_German_Market(language="German", warning_flag=False, temp_market_display= "Fahrenhiet")

  #Object initialisation Battery Management System
  Object_BMS_Temperature_India= Battery_Management_System(0,45,5, Object_Indian_Market)
  Object_BMS_SOC_India= Battery_Management_System(20,80, 5, Object_Indian_Market)
  Object_BMS_ChargeRate_India= Battery_Management_System(0,0.8, 0, Object_Indian_Market)

  Object_BMS_Temperature_German= Battery_Management_System(0,45,5, Object_German_Market)
  Object_BMS_SOC_German= Battery_Management_System(20,80, 5, Object_German_Market)
  Object_BMS_ChargeRate_German= Battery_Management_System(0,0.8, 0, Object_German_Market)
  
  
  Object_Battery_Tester = Test_Battery_OK()

  print("\n\nTemperature Range Warning Test")
  #Set 1 -> Valid Range Temperature
  Object_Battery_Tester.Tester(Object_BMS_Temperature_German, -2, "Low_Breach")
  Object_Battery_Tester.Tester(Object_BMS_Temperature_India, 2, "Low_Warning")
  Object_Battery_Tester.Tester(Object_BMS_Temperature_German, 10, "Normal")
  Object_Battery_Tester.Tester(Object_BMS_Temperature_India, 43, "High_Warning")
  Object_Battery_Tester.Tester(Object_BMS_Temperature_India, 50, "High_Breach")

  print("\n\nSOC Range Warning Test")
  #Set 2 -> Valid Range SOC
  Object_Battery_Tester.Tester(Object_BMS_SOC_India, 0, "Low_Breach")
  Object_Battery_Tester.Tester(Object_BMS_SOC_India, 22, "Low_Warning")
  Object_Battery_Tester.Tester(Object_BMS_SOC_German, 30, "Normal")
  Object_Battery_Tester.Tester(Object_BMS_SOC_India, 77, "High_Warning")
  Object_Battery_Tester.Tester(Object_BMS_SOC_India, 85, "High_Breach")

  print("\n\nChargeRate Range Warning Test")
  #Set 3 -> Valid Range ChargeRate
  Object_Battery_Tester.Tester(Object_BMS_ChargeRate_India, -0.5, "Low_Breach")
  Object_Battery_Tester.Tester(Object_BMS_ChargeRate_German, 0.3, "Normal")
  Object_Battery_Tester.Tester(Object_BMS_ChargeRate_India, 0.9, "High_Breach")

  print("All is well!")

