"""


[Goldbach's Conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)
is amongst the oldest and well-known unsolved mathematical problems. In
correspondence with [Leonhard
Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) in 1742, German
mathematician [Christian
Goldbach](https://en.wikipedia.org/wiki/Christian_Goldbach) made a conjecture,
which states:

 **"Every even whole number greater than 2 is the sum of two prime numbers."**

Even though it's been thoroughly tested and analyzed and seems to be true, it
hasn't been proved yet (thus, remaining a conjecture.)

Create a function that takes a number and returns an array as per the
following rules:

  * If the given number is odd and greater than two, return an empty array.
  * If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
  * Both prime numbers must be the farthest (with the greatest difference).

### Examples

    goldbach_conjecture(1) ➞ []
    # The given number is not greater than 2.
    
    goldbach_conjecture(7) ➞ []
    # The given number is not an even number.
    
    goldbach_conjecture(14) ➞ [3, 11]

### Notes

Return list in sequence: `[smaller, bigger]`

"""

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
def goldbach_conjecture(n):
​
  if (n < 2) or (n % 2 != 0) or (n % 1 != 0):
    return []
    
  else:
    Value = 2
    Ceiling = n
    
    while (Value < Ceiling):
      Difference = n - Value
      Test_A = FNC_Prime_Number_Checker(Value)
      Test_B = FNC_Prime_Number_Checker(Difference)
      
      if (Test_A and Test_B):
        Answer = []
        Answer.append(Value)
        Answer.append(Difference)
        return Answer
      else:
        Value += 1
        
    return []

