"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

def gcf(n1, n2): 
  cf_list = []
  if n2 > n1:
    for f in range(1, n1+1):
      if n1 % f == 0 and n2 % f == 0:
        cf_list.append(f)
    return max(cf_list)
  else:
    for f in range(1, n2+1):
      if n1 % f == 0 and n2 % f == 0:
        cf_list.append(f)
    return max(cf_list)
​
def simplify(txt):
  list_nums = txt.split('/')
  N = int(list_nums[0])
  D = int(list_nums[1])
  if (N/D) % 1 == 0:
    return str(int(N/D))
  else:
    top = str(int(N/gcf(N,D)))
    bottom = str(int(D/gcf(N,D)))
    return top + '/' + bottom

