"""


Create a function that takes a list of numbers and returns the _greatest
common factor_ of those numbers.

### Examples

    gcd([84, 70, 42, 56]) ➞ 14
    
    gcd([19, 38, 76, 133]) ➞ 19
    
    gcd([120, 300, 95, 425, 625]) ➞ 5

### Notes

The GCD is the largest factor that divides all numbers in the list.

"""

def gcd(arr):
  def find_factors(num):
    return list(reversed([n for n in range(2, num+1) if num % n == 0] ))
  
  all_divisors = [find_factors(n) for n in arr]
  shortest = [div for div in all_divisors if len(div) == min([len(d) for d in all_divisors])][0]
  
  for n in range(len(shortest)):
    item = shortest[n]
    print(item)
    poss = True
    for divisor in all_divisors:
      if item not in divisor:
        poss = False
        break
    if poss == True:
      return item
  
  return 1

