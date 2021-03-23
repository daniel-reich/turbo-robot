"""


Write a program that returns a list of all the numbers from 1 to an integer
argument. But for multiples of three use “Fizz” instead of the number and for
the multiples of five use “Buzz”. For numbers which are multiples of both
three and five use “FizzBuzz”.

### Example

    fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
    
    fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

### Notes

Make sure to `return` a list.

"""

def fizz_buzz(maximum):
​
  returnlist = []
​
  for a in range(1, maximum+1):
    if (a % 5 == 0) & (a % 3 == 0):
      returnlist.append('FizzBuzz')
    elif a % 5 == 0:
      returnlist.append('Buzz')
    elif a % 3 == 0:
      returnlist.append('Fizz')
    else:
      returnlist.append(a)
      
  return returnlist

