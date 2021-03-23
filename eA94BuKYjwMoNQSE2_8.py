"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

def correct_signs(txt):
  x = [i for i in txt if i in '<>']
  t = txt.replace(' <', '').replace(' >', '').split()
  return all(int(t[i])<int(t[i+1]) if x[i]=='<' else int(t[i])>int(t[i+1]) for i in range(len(t)-1))

