FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    print(f"{fahrenheit}°F is {(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

def convert_to_fahrenheit(celsius):
    print(f"{celsius}°C is {(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+ 32}°F")

temperature = input("Enter the temperature to convert: ")
if temperature.isnumeric()!= True:
    print("Invalid temperature. Please enter a numeric value.")
else:
    temp_type= input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if temp_type == "c":
        convert_to_fahrenheit(temperature)
    else:
        convert_to_celsius(temperature)