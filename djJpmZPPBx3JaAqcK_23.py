"""


Maya numeral system was **vigesimal** ( _base 20_ ) and **positional** :
units, tens, hundreds (and so on) were read as descendant progressive powers
of 20, instead of 10 like we do with our decimal system. Some examples:

    - 39 => (1 x 20¹) + (19 x 20º)
    - 815 => (2 x 20²) + (0 x 20¹) + (15 x 20º)
    - 16125 => (2 x 20³) + (0 x 20²) + (6 x 20¹) + (5 x 20º)

Every digit (as to say the number to be multiplied for the power of 20) was
symbolized with a combination of pebbles (dots), woodsticks (lines) and shells
(used for the number 0) following a _base5_ system. See the table below:

![Mayan Numbers](https://edabit-challenges.s3.amazonaws.com/maya_numbers.jpg)

You must implement a function that, given a non-negative integer, returns a
list of strings, with each string representing the symbolized single digit.

Symbols to use are " **@** " for shells, " **-** " for lines and " **o** " for
dots. Dots have to be placed **before** the lines.

### Examples

    # Be careful, spaces between symbols are placed only for better readability!
    # Don't use spaces in returned strings.
    
    maya_number(39) ➞ ["o", "o o o o - - -"]
    
    maya_number(815) ➞ ["o o", "@", "- - -"]
    
    maya_number(16125) ➞ ["o o", "@", "o -", "-"]

### Notes

  * Check the **Resources** tab for more info on Maya numerals (and Maya arithmetic).
  * All given integers are valid, no exceptions to handle.

"""

def maya_number(n):
  
  class Base:
​
    def __init__(self, base):
      self.b = base
    
    def convert(self, b10num):
​
      divisors = [1]
      exp = 1
      while max(divisors) <= b10num:
        divisors.append(self.b ** exp)
        exp += 1
      
      divisors = list(reversed(divisors))[1:]
​
      digits = []
​
      for divisor in divisors:
        digit = int(b10num / divisor)
        digits.append(digit)
        b10num = b10num % divisor
      
      return digits
  def convert_to_maya(number):
    ints = list(sorted(range(0, 20)))
    maya = '@ o oo ooo oooo - o- oo- ooo- oooo- -- o-- oo-- ooo-- oooo-- --- o--- oo--- ooo--- oooo---'.split()
​
    int_to_maya = {}
​
    for n in range(20):
      int_to_maya[ints[n]] = maya[n]
    
    mayan_digits = []
​
    for digit in number:
      mayan_digits.append(int_to_maya[digit])
    
    return mayan_digits
​
  if n == 0:
    return ['@']
  
  b = Base(20)
  converted = b.convert(n)
​
  return convert_to_maya(converted)

