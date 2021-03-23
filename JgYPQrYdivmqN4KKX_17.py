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
  if weight.split()[1] == 'pounds':
    weight = float(weight.split()[0]) * 0.453592
  else:
    weight = float(weight.split()[0])
  if height.split()[1] == 'inches':
    height = float(height.split()[0]) * 0.0254
  else:
    height = float(height.split()[0])
  bmi = round(weight/(height**2),1)
  if bmi < 18.5:
    return str(bmi) + ' Underweight'
  elif 18.5 <= bmi <= 24.9:
    return str(bmi) + ' Normal weight'
  elif 25 <= bmi <= 29.9:
    return str(bmi) + ' Overweight'
  else:
    return str(bmi) + ' Obesity'

