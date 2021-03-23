"""


Write a program that takes a temperature input in `celsius` and converts it to
**Fahrenheit** and **Kelvin**. Return the converted temperature values in a
list.

The formula to calculate the temperature in Fahrenheit from Celsius is:

    F = C*9/5 +32

The formula to calculate the temperature in Kelvin from Celsius is:

    K = C + 273.15

### Examples

    temp_conversion(0) ➞ [32, 273.15]
    # 0°C is equal to 32°F and 273.15 K.
    
    temp_conversion(100) ➞ [212, 373.15]
    
    temp_conversion(-10) ➞ [14, 263.15]
    
    temp_conversion(300.4) ➞ [572.72, 573.55]

### Notes

  * Return calculated temperatures up to two decimal places.
  * Return `"Invalid"` if K is less than 0.

"""

def temp_conversion(celsius):
  lst = []
  lst.append(round(celsius*9/5 +32, 2))
  lst.append(round(celsius + 273.15, 2))
  if lst[1] <= 0:
    return "Invalid"
  return lst

