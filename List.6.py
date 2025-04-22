fahrenheit_temperatures = [32, 68, 100, 50, 72]
print("Temperatures in Fahrenheit:", fahrenheit_temperatures)

celsius_temperatures = [(temp - 32) * 5.0/9.0 for temp in fahrenheit_temperatures]

print("Temperatures in Celsius:", celsius_temperatures)
