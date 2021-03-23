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
  wt=weight.split()
  ht=height.split()
  if wt[-1]=="pounds":
    w=float(wt[0])*0.453592
  else:
    w=float(wt[0])
  if ht[-1]=="inches":
    h=float(ht[0])*0.0254
  else:
    h=float(ht[0])
  BMI=round(w/h**2,1)
  if BMI<18.5:
    BMIt="Underweight"
  elif 18.5<=BMI<25:
    BMIt="Normal weight"
  elif 25<=BMI<30:
    BMIt="Overweight"
  else:
    BMIt="Obesity"
  return "{} {}".format(BMI,BMIt)

