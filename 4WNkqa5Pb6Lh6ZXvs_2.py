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

def evaluate_polynomial(poly, num):
  out=''
  if  len([c for c in poly if c=='('])!=len([c for c in poly if c==')']) or \
  sum([1 for s in ['#','$','//','%','|','&','print'] if s in poly])>0 or len(poly)==0:
    return 'invalid'
  for i in range(len(poly)):
    if poly[i]== 'x':
      if i< len(poly)-1 and i>0:
        if poly[i-1].isnumeric():
          if poly[i+1].isnumeric() or poly[i+1]=='(':
            out+='*' + str(num) + '*'
          else:
            out+='*' + str(num)
        elif (poly[i+1].isnumeric() or poly[i+1]=='(') and not poly[i-1].isnumeric():
          out+=str(num) + '*'
        else:
          out+=str(num)
      else:
        if i==0:
          if (i+1 < len(poly)-1):
            if (poly[i+1].isnumeric() or poly[i+1]=='('):
              out+=str(num) + '*'
            else:
              out+=str(num)
          else:
            out+=str(num)
        else:
          if(i-1 >=0):
            if poly[i-1].isnumeric() or poly[i-1]==')':
              out+='*' + str(num)
            else:
              out+= str(num)
          else:
            out+= str(num)
​
    else:
      if (poly[i]=='^'):
        out+='**'
      elif (poly[i].isnumeric()):
        if (i+1 < len(poly)-1):
          if poly[i+1]=='(':
            out+=poly[i]+'*'
          else:
            out+=poly[i]
        else:
          out+=poly[i]
      else:
        out+=poly[i]
  return round(eval(out))

