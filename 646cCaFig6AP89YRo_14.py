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
  b = []
  for i in range(1,maximum+1):
    if i%3 == 0 and i%5 == 0:
      a = "FizzBuzz"
      b.append(a)
    elif i%3 == 0:
      a = "Fizz"
      b.append(a)
    elif i%5 == 0:
      a = "Buzz"
      b.append(a)
    else:
      a = i
      b.append(a)
  return b

