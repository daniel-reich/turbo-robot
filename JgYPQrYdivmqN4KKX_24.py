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

inch  = 0.0254
pound = 0.453592
def BMI(weight, height):
  w_s, w_system = weight.split()
  h_s, h_system = height.split()
  
  w = float(w_s) * (pound if w_system == 'pounds' else 1)
  h = float(h_s) * (inch  if h_system == 'inches' else 1)
  
  bmi = w / h ** 2
  if           bmi < 18.5: category = 'Underweight'
  elif 18.5 <= bmi < 24.9: category = 'Normal weight'
  elif   25 <= bmi < 29.9: category = 'Overweight'
  else:                    category = 'Obesity'
  
  return '{0} {1}'.format(round(bmi, 1), category)

