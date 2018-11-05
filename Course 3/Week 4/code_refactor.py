"""
Converting the average daily temperatures for several planets 
from Kelvin to Farenheit --- Version 0
"""


# Initialize emperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
mercury_result = (mercury - 275.15) * 9 / 5 + 32
venus_result = (venus - 275.15) * 9 / 5 + 32
mars_result = (mars - 275.15) * 9 / 5 + 32

# Print
print("The daily average temperature on Mercury is", mercury_result, "Farenheit")
print("The daily average temperature on Venus is", venus_result, "Farenheit")
print("The daily average temperature on Mars is", mars_result, "Farenheit")

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit