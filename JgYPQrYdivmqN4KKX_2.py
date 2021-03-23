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
  weight, weight_unit = weight.split()
  height, height_unit = height.split()
  weight_modifier, height_modifier = 1, 1
  if weight_unit == 'pounds':
    weight_modifier = 0.453592
  if height_unit == 'inches':
    height_modifier = 0.0254
  weight = float(weight) * weight_modifier
  height = float(height) * height_modifier
  bmi = weight / (height**2)
  if bmi < 18.5:
    bmi_description = 'Underweight'
  elif bmi <= 24.9:
    bmi_description = 'Normal weight'
  elif bmi <= 29.9:
    bmi_description = 'Overweight'
  else:
    bmi_description = 'Obesity'
  return '{:0.1f} {}'.format(bmi, bmi_description)

