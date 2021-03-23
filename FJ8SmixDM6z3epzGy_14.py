"""


Create a function that tests whether or not an integer is a **perfect
number**. A perfect number is a number that can be written as the sum of its
factors, excluding the number itself.

For example, 6 is a **perfect number** , since 1 + 2 + 3 = 6, where 1, 2, and
3 are all factors of 6. Similarly, 28 is a **perfect number** , since 1 + 2 +
4 + 7 + 14 = 28.

### Examples

    check_perfect(6) ➞ True
    
    check_perfect(28) ➞ True
    
    check_perfect(496) ➞ True
    
    check_perfect(12) ➞ False
    
    check_perfect(97) ➞ False

### Notes

N/A

"""

def check_perfect(number):
  
  # Local variables 
  count = 0
  sum = 0
  
  # Loop from 0 to number 
  for i in range(0, number):
    # Increase the count by one 
    count += 1
    
    # Check if count is a factor of number 
    if number % count == 0 and count != number:
      # Sum up the count and store in variable 
      sum += count
  
  # Check if sum is equal to number 
  if sum == number:
    # Return true 
    return True
  
  # Return false 
  return False

