"""


A modified Kaprekar number is a positive whole number with a special property.
If you square it, then split the number into two integers and sum those
integers, you have the same value you started with.

Consider a positive whole number `n` with `d` digits. We square `n` to arrive
at a number that is either `2 * d` digits long or `(2 * d) - 1` digits long.
Split the string representation of the square into two parts, `l` and `r`. The
right-hand part, `r` must be `d` digits long. The left is the remaining
substring. Convert those two substrings back to integers, add them and see if
you get `n`.

For example, if `n=5`, `d=1`, then `n` squared = `25` . We split that into two
strings and convert them back to integers `2` and `5`. We test `2+5=7=5`, so
this is not a modified Kaprekar number. If `n=9`, `d=1`, and `n` squared =
`81`. This gives us `1+8=9`, the original `n`.

Note that `r` may have leading zeros.

Complete the `kaprekar_numbers()` method. It should return the list of
modified Kaprekar numbers in ascending order. `kaprekar_numbers()` has the
following parameter(s):

  * `p`: an integer representing the lower integer limit.
  * `q`: an integer representing the upper integer limit.

### Examples

    kaprekar_numbers(1, 10) ➞ "1 9"
    
    kaprekar_numbers(100, 300) ➞ "297"
    
    kaprekar_numbers(1, 100) ➞ "1 9 45 55 99"

### Notes

  * Upper and lower ranges should be inclusive of the limits.
  * If no modified Kaprekar numbers exist in the given range, return `"INVALID RANGE"`.

"""

def kaprekar_numbers(p, q):
  def is_kaprekar(num):
    squared = str(num ** 2)
    d = len(str(num))
​
    if len(squared) == 2*d:
      l = squared[:d]
      r = squared[d:]
    elif len(squared) == (2*d) - 1:
      l = squared[:d-1]
      r = squared[d-1:]
    else:
      print('ERROR!')
    
    try:
      return int(l) + int(r) == num
    except ValueError:
      return 0 + int(r) == num
  
  kaprekars = []
  
  for n in range(p, q+1):
    if is_kaprekar(n) == True:
      kaprekars.append(str(n))
  
  if len(kaprekars) == 0:
    return 'INVALID RANGE'
  else:
    return ' '.join(kaprekars)

