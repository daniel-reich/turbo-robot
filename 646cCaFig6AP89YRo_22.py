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

def fizz_buzz(n):
  return [i if (i%3)*(i%5) else 'Fizz'*(not i%3)+'Buzz'*(not i%5) for i in range(1, n+1)]

