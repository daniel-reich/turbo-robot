"""


Declare a `division()` function that gets two natural numbers (`a`, `b`) and
return a string containing the rational number `a` / `b` in the form of a
decimal fraction, possibly **periodic**.

### Examples

    division(2, 5) ➞ "0.4"
    
    division(1, 6) ➞ "0.1(6)"
    
    division(1, 3) ➞ "0.(3)"
    
    division(1, 7) ➞ "0.(142857)"
    
    division(1, 77) ➞ "0.(012987)"

### Notes

  * The length of a periodic fraction can be more than **20 numbers**.
  * The function should be efficient.

"""

def division(a,b):
  d, s, w = '', str(a//b)+'.', 4
  while a%b:
    a = a%b*10
    d += str(a//b)
    if d[-w:] in d[:-w]: break
  if not d: d='0'
  if a%b==0: return s+d
  i = d.find(d[-w:])
  r = d[i:-w]
  j = (r+r).find(r, 1,-1) 
  if j!=-1: r = r[:j]
  return s+d[:i]+'('+r+')'

