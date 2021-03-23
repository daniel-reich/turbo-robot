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

def express_factors(n):
  cat = []
  wrt = get_factors(n)
  cha = sorted(set(wrt),key=wrt.index)
  arr =[[x,wrt.count(x)] for x in cha]
  for i in range(0,len(arr)):
    if arr[i][1]==1:
      cat.append(str(arr[i][0]))
    else:
      cat.append("{}^{}".format(arr[i][0],arr[i][1]))
  return " x ".join(cat)
def get_factors(x):
  lst = []
  for i in range(2, x+1):
    while x%i==0:
      lst.append(i)
      x = x//i
    if x==1:
      break
  return lst

