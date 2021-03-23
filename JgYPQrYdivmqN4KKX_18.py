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
  if "kilos" in weight:
    fBmi = round(float(weight.split()[0]) / float(height.split()[0])**2,1)
  else : 
    a = (float(weight.split()[0])) * 0.453592
    b = (float(height.split()[0])) * 0.0254
    fBmi = round(a/b**2,1)
  
  if fBmi < 18.5:
    return "{0} Underweight".format(fBmi)
  elif fBmi >= 18.5 and fBmi < 24.9:
    return "{0} Normal weight".format(fBmi)
  elif fBmi >= 25 and fBmi < 29.9:
    return "{0} Overweight".format(fBmi)
  elif fBmi >= 30:
    return "{0} Obesity".format(fBmi)

