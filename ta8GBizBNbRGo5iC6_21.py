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
  def add(self, a, b):
    return a + b
  def subtract(self ,a, b):
    return a - b
  def multiply(self, a, b):
    return a * b
  def divide(self, a, b):
    return a / b

