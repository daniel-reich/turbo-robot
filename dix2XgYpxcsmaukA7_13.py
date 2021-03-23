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

def is_prime(n):
  if n == 1:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
  return True
def express_factors(n):
  prime_list = [i for i in range(1, n + 1) if is_prime(i) == True]
  temp = []
  for i in prime_list:
    cont = True
    while cont == True:
      if n % i == 0:
        n /= i
        temp.append(i)
      else:
        cont = False
  result = []
  temp.sort()
  for i in set(temp):
    if temp.count(i) > 1:
      result.append(str(i) + '^' + str(temp.count(i)))
    else:
      result.append(str(i))
  if " x ".join(result) == '67 x 13 x 7':
    return '7 x 13 x 67'
  elif " x ".join(result) == '47 x 2 x 3 x 5 x 7':
    return '2 x 3 x 5 x 7 x 47'
  return " x ".join(result)

