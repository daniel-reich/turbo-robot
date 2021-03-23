"""


You will be given a polynomial expression in string form. The expression will
contain any of the following operations, written using standard mathematical
notation for a single variable, "x", as illustrated in the examples below:

  * addition: x + 1
  * subtraction: x – 2
  * multiplication: 3x
  * division: x / 4
  * exponentation: x^5
  * brackets: x(x + 1)

Your task is to write a function that can evaluate such a polynomial for a
given value of x. You will receive two arguments: the polynomial string and
the input number.

If the mathematical expression contains an error, you should return
`"invalid"`.

### Examples

    evaluate_polynomial("x+1", 5) ➞ 6
    
    evaluate_polynomial("5x^2", 3) ➞ 45
    
    evaluate_polynomial("(x(x+1))/2", 4) ➞ 10
    
    evaluate_polynomial("4(x + 3))/2", 5) ➞ "invalid"
    # Invalid because parentheses not balanced.

### Notes

The string will not contain spaces.

"""

allowed = "0123456789()+-*/^x"
def evaluate_polynomial(poly, num):
    if any([c not in allowed for c in poly]) or len(poly.strip()) == 0:
        return "invalid"
    poly = poly.replace('^', '**').replace('x(', 'x*(').replace('/', '//')
    for d in range(10):
        poly = poly.replace(str(d) + '(', str(d) + '*(')
        poly = poly.replace(str(d) + 'x', str(d) + '*x')
    poly = poly.replace('x', str(num))
    try:
        ans = eval(poly)
        return ans
    except:
        return "invalid"

