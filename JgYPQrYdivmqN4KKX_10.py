"""


Body Mass Index (BMI) is found by taking your weight in kilograms and dividing
by the square of your height in meters. The BMI categories are:

  * Underweight: <18.5
  * Normal weight: 18.5–24.9
  * Overweight: 25–29.9
  * Obesity: BMI of 30 or greater

Create a function that will accept weight and height (in kilos, pounds,
meters, or inches) and return the BMI and the associated category. Round the
BMI to nearest tenth.

### Examples

    BMI("205 pounds", "73 inches") ➞ "27.0 Overweight"
    
    BMI("55 kilos", "1.65 meters") ➞ "20.2 Normal weight"
    
    BMI("154 pounds", "2 meters") ➞ "17.5 Underweight"

### Notes

  * 1 inch = 0.0254 meter
  * 1 pound = 0.453592 kilo

"""

def BMI(weight, height):
  weight_value, weight_unit = weight.split()
  height_value, height_unit = height.split()
  weight_value = float(weight_value)
  height_value = float(height_value)
  if weight_unit == "pounds":
    weight_value *= 0.453592
  if height_unit == "inches":
    height_value *= 0.0254
  bmi = round(weight_value/height_value**2,1)
  if bmi < 18.5:
    return str(bmi) + " Underweight"
  if 18.5<=bmi<25:
    return str(bmi) + " Normal weight"
  if 25<=bmi<30:
    return str(bmi) + " Overweight"
  else:
    return str(bmi) + " Obesity"

