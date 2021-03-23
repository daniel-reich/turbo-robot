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
  result = []
  for i in range(maximum):
    i = i+1
    fizz = buzz = False
    if i%3==0:
      fizz = True
    if i%5 == 0:
      buzz = True
    if fizz and buzz:
      result.append("FizzBuzz")
    elif fizz:
      result.append("Fizz")
    elif buzz:
      result.append("Buzz")
    else:
      result.append(i)
  print(result)
  return(result)

