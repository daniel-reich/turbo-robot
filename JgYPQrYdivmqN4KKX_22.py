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
  in2m = 0.0254
  p2k = 0.453592
  n = weight.rfind(' kilos')
  if n > 0:
    w = float(weight[:n])
  else:
    n = weight.rfind(' pounds')
    if n > 0:
      w = float(weight[:n]) * p2k
  n = height.rfind(' meters')
  if n > 0:
    h = float(height[:n])
  else:
    n = height.rfind(' inches')
    if n > 0:
      h = float(height[:n]) * in2m
  bmi = round(w / h**2, 1)
​
  if bmi < 18.5:
    s = 'Underweight'
  elif bmi < 25:
    s = 'Normal weight'
  elif bmi < 30:
    s = 'Overweight'
  else:
    s = 'Obesity'
  return '{} {}'.format(bmi, s)

