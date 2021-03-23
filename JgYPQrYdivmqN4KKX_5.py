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
    w, h = weight.split(), height.split()
    if w[1] == 'kilos':
        w[0] = float(w[0]) * 2.20462
    if h[1] == 'meters':
        h[0] = float(h[0]) * 39.3701
​
    bmi = round(703 * float(w[0]) / float(h[0]) ** 2, 1)
​
    if bmi < 18.5:
        return '{} Underweight'.format(bmi)
    elif bmi < 25:
        return '{} Normal weight'.format(bmi)
    elif bmi < 30:
        return '{} Overweight'.format(bmi)
    else:
        return '{} Obesity'.format(bmi)

