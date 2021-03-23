"""


Given a list of _math equations_ (given as strings), return the **percentage
of correct answers** _as a string_. Round to the nearest _whole number_.

### Examples

    mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"
    
    mark_maths(["1-2=-2"]), "0%"
    
    mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"

### Notes

  * You can expect only _addition_ and _subtraction_.
  * Note how there aren't any spaces in any given equation.

"""

def mark_maths(lst):
  initial = [int(x[int(x.find('=') + 1):]) for x in lst]
  cut_off = [x[:int(x.find('='))] for x in lst]
  evaluated = [eval(x) for x in cut_off]
  final = []
  for a, b in zip(initial, evaluated):
    if a == b:
      final.append(a)
  return '{}%'.format(round(len(final) / len(lst) * 100))

