"""


Replace the numbers in a string with their binary form.

### Examples

    replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."
    
    replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."
    
    replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"

### Notes

  * There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
  * Anything separates two numbers, even spaces ("2 2" --> "10 10").

"""

def replace_nums(string):
  import re
  def digitrepl(match):
    value = int(match.group())
    return getBin(value)
    
  def getBin(i =0):
    s = []
    j=i
    if i == 0:
      return '0'
    else:
      while j > 0:
        s.append( j % 2 )
        j= j // 2
      return ''.join(str(k) for k in reversed(s))
  p = re.compile(r'\d+')
  return p.sub(digitrepl,string)

