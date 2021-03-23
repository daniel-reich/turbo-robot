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

def evaluate_polynomial(poly,num):
  for i in range (len(poly)):
    if not poly[i].isnumeric() and not poly[i] in "+-/^()x" or (poly[i]=="/" and poly[i+1]=="/"):
      return "invalid"
  try:
    poly = poly.replace("^","**")
    for i in range (len(poly)-1):
      if (poly[i].isnumeric() or poly[i] in "x)") and poly[i+1] in "x(":
        poly = poly[:i+1]+"*"+poly[i+1:]
    return eval(poly,{},{"x":num})
  except:
    return "invalid"

