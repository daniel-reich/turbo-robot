"""


A number is said to be Disarium if the **sum** of its _digits raised to their
respective positions_ is the number itself.

Create a function that determines whether a number is a Disarium or not.

### Examples

    is_disarium(75) ➞ False
    # 7^1 + 5^2 = 7 + 25 = 32
    
    is_disarium(135) ➞ True
    # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
    
    is_disarium(544) ➞ False
    
    is_disarium(518) ➞ True
    
    is_disarium(466) ➞ False
    
    is_disarium(8) ➞ True

### Notes

  * Position of the digit is 1-indexed.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/aifM22oGtRKShsFWB).

"""

def is_disarium(number):
  
  # Local variables 
  position = 0
  product = 1
  sum = 0
  
  # Turn number into string and store in variable 
  number = str(number)
  
  # Loop through the number 
  for digit in number:
    # Increase value of position by one 
    position += 1
    
    # Get the number and turn to integer 
    digit = int(digit)
    
    # Loop from 0 to position 
    for i in range(0, position):
      # Get the product and store in variable 
      product *= digit
    
    # Sum up the product
    sum += product 
    
    # Reset the value of product to one 
    product = 1
  
  # Turn number back to integer 
  number = int(number)
  
  # Check if sum equals number 
  if sum == number:
    # Return true 
    return True
  
  # Return false 
  return False

