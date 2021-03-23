"""


Create a function that takes a positive integer and returns a string
expressing how the number can be made by multiplying powers of its prime
factors.

### Examples

    express_factors(2) ➞ "2"
    
    express_factors(4) ➞ "2^2"
    
    express_factors(10) ➞ "2 x 5"
    
    express_factors(60) ➞ "2^2 x 3 x 5"

### Notes

  * All inputs will be positive integers in the range 1 < n < 10,000.
  * If a factor is repeated express it in the form **"x^y"** where x is the factor and y is the number of repetitions of the factor.
  * If `n` is a prime number, return `n` as a string as in example #1 above.
  * Factors should appear in ascending order in the expression.
  * Make sure you include the space either side of the multiplication sign, `" x "`.
  * Check the **Resources** if you need to understand **Prime Factorization**.

"""

############################################################
#     Sub Function 
############################################################
​
def FNC_Prime_Number_Checker(Number):
​
  Divisor = 2
  
  while (Divisor < Number):
    
    if (Number % Divisor == 0):
      return False
    else:
      Divisor += 1
      
  return True
​
############################################################
#     MAIN FUNCTION
############################################################
​
def express_factors(n):
  
  Prime_Factors = []
  
  Divisor = 2
  Remaining = n
  
  while (Remaining > 1):
    
    Test_A = FNC_Prime_Number_Checker(Divisor)
    Test_B = Remaining % Divisor
    
    if (Test_A == True) and (Test_B == 0):
      Prime_Factors.append(Divisor)
      Remaining /= Divisor
    else:
      Divisor += 1
  
  Checked = []
  Equation = []
  
  Counter = 0
  Length = len(Prime_Factors)
  
  while (Counter < Length):
    
    Number = Prime_Factors[Counter]
    Power = Prime_Factors.count(Number)
    
    if (Number not in Checked) and (Power > 1):
      Passage = str(Number) + "^" + str(Power)
      Equation.append(Passage)
      Checked.append(Number)
      Counter += 1
    elif (Number not in Checked) and (Power == 1):
      Passage = str(Number)
      Equation.append(Passage)
      Checked.append(Number)
      Counter += 1
    else:
      Counter += 1
      
  Link = " x "
  Answer = Link.join(Equation)
  return Answer

