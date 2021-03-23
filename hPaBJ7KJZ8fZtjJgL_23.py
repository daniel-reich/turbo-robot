"""


Write a function that takes an integer and returns a string with the given
number of `"a"`s in Edabit.

### Examples

    how_many_times(5) ➞ "Edaaaaabit"
    
    how_many_times(0) ➞ "Edbit"
    
    how_many_times(12) ➞ "Edaaaaaaaaaaaabit"

### Notes

  * The string must start with "Ed" and end with "bit".
  * You'll only be given integers as test input.

"""

def how_many_times(num):
  return "Ed" + "a" * num + "bit"

