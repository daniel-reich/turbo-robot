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
​
  def add(self, n1, n2):
    return n1 + n2
  
  def subtract(self, n1, n2):
    return n1 - n2
    
  def multiply(self, n1, n2):
    return n1 * n2
  
  def divide(self, n1, n2):
    return n1 / n2

