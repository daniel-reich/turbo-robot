"""


Create a function that takes a string and returns a new string with each new
character accumulating by +1. Separate each set with a dash.

### Examples

    accum("abcd") ➞ "A-Bb-Ccc-Dddd"
    
    accum("RqaEzty") ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    
    accum("cwAt") ➞ "C-Ww-Aaa-Tttt"

### Notes

  * Capitalize the first letter of each set.
  * All tests contain valid strings with alphabetic characters (a-z, A-Z).

"""

def accum(txt):
  output = map(lambda x: x[1] * x[0], enumerate(list(txt),1))
  output = [x.capitalize() for x in output]
  return '-'.join(output)

