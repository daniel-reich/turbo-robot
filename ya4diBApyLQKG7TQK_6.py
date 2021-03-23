"""


You will be given a string consisting of a list of integers and their
relationships to their neighboring integers. For instance:

    "-15<-10<=0=0<5"

Test to see that all the relationships between the integers in the string are
true. If they are, return `True`. If they are not, return `False`.

### Examples

    validate_relationships("5>-1<0=0<-5>5=5") ➞ False
    # This is False because 0 is not less than -5.
    
    validate_relationships("-15<-10<=0=0<5") ➞ True
    
    validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
    # This is False because 0 is not equal to 807.

### Notes

  * This is a modifcation of Helen Yu's "Correct Signs" challenge.
  * As the examples above show, there could be negative numbers in the string.
  * The numbers will only be separated by: `=, <, >, >=, <=`
  * Tests will not contain any spaces.

"""

def validate_relationships(txt):
  s, v, t = [], 1, txt[0]
  if t in '0123456789-':
    v = 0
  for i in txt[1:]:
    if i in '0123456789-' and v == 0:
      t += i
    elif i in '0123456789-' and v == 1:
      s.append(t)
      t, v = i, 0
    elif i not in '0123456789-' and v == 0:
      s.append(t)
      t, v = i, 1
    else:
      t += i
  s.append(t)
  for g in range(0, len(s) - 2, 2):
    k1 = int(s[g])
    k2 = int(s[g + 2])
    if s[g + 1] == '>':
      if k1 <= k2:
        return False
    elif s[g + 1] == '>=':
      if k1 < k2:
        return False
    elif s[g + 1] == '=':
      if k1 != k2:
        return False
    elif s[g + 1] == '<=':
      if k1 > k2:
        return False
    else:
      if k1 >= k2:
        return False
  return True

