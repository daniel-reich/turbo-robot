"""


Create methods for the `Calculator` class that can do the following:

  * Add two numbers.
  * Subtract two numbers.
  * Multiply two numbers.
  * Divide two numbers.

### Examples

    calculator = Calculator()
    
    calculator.add(10, 5) ➞ 15
    
    calculator.subtract(10, 5) ➞ 5
    
    calculator.multiply(10, 5) ➞ 50
    
    calculator.divide(10, 5) ➞ 2

### Notes

  * The methods should return the result of the calculation.
  * Don't worry about needing to handle division by zero errors.
  * See the **Resources** tab for some helpful tutorials on Python classes.

"""

class Calculator:
  # Write methods to add(), subtract(), multiply() and divide()
  
  def __init__(self,num1=0,num2=0):   
    self.num1=num1
    self.num2=num2
  def add(self,num1,num2):
    return num1+num2
  def subtract(self,num1,num2):
    return num1-num2
  def multiply(self,num1,num2):
    return num1*num2
  def divide(self,num1,num2):
    return num1/num2

