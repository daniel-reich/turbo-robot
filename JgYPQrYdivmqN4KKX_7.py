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
    w_lst=weight.split()
    h_lst=height.split()
   # print(w_lst,' ',h_lst)
    if w_lst[1] == "pounds":
        kg=int(w_lst[0])*0.453592
    else: 
        kg=float(w_lst[0])
    if h_lst[1] == "inches":
        m=int(h_lst[0])*0.0254
    else:
        m=float(h_lst[0])
    bmi=round((kg/(m**2)),1)
    #print(bmi)
    if bmi < 18.5:
        output="Underweight"
    elif bmi < 24.9:
        output="Normal weight"
    elif bmi < 29.9:
        output="Overweight"
    else:
        output="Obesity"
    return str(bmi)+' '+output

