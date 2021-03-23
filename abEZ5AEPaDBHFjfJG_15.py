"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

#formula("6 * 4 = 24") -> True
#formula("18 / 17 = 2") -> False
#formula("") -> None
#formula('(1+2+3+4+5+6+7+8)/a=9') -> True
#formula('2 * 2 * 2 = a * 2 = 8') -> True
#formula('a = a') -> True
​
def isNumber(value):
  try:
    float(value)
    return True
  except:
    return False
​
def getValueA(a,b):
  index = a.find("a")
  if len(a[index+1:]) >= 2: # a 
    rAop = a[index+1:index+2]     
    if rAop == "/": # a / 3 = 9
      
      return True
      #return (a[index+2:] * compute(b))
    if rAop == "*": # a * 4 = 8
      return compute(b) % compute(a[index+2:]) == 0
    if rAop == "+" or  rAop == "-": # a + 5 = 54
      return True
  elif len(a[0:index-2]) >= 2:  # 
    lAop = a[index-2:index-1]
    if lAop == "/": # 65 / a = 98
      return compute(a[0:index-2]) % compute(b)
    if lAop == "*":  # 65 * a = 87
      return compute(b) % compute(a[0:index-2]) == 0
    if lAop == "+" or  lAop == "-":
      return True 
  return True
    
def equation(a,b):
  if a.find("a") != -1 and b.find("a") != -1:
    if len(a) >= 2 and len(b) >=2:
      return compute(a) == compute(a)
    return a == b
    
  #  334-a*434 = 54645  
  if a.find("a") != -1 and b.find("a") == -1:
    return getValueA(a,b)       
  if b.find("a") != -1 and a.find("a") == -1:
    return getValueA(b,a)
    
  return compute(a) == compute(b) 
def equalsOperation(a,b):
  #more than 2 equal signs. 
  if a.find("=") != -1 and b.find("=") == -1 :
    index = a.find("=")
    return equation(a[0:index], a[index+1:]) \
            and equation(b,a[index+1:])
​
  if a.find("=") == -1 and b.find("=") != -1 :
    index = b.find("=")
    return equation(b[0:index], b[index+1:]) \
            and equation(a ,b[index+1:])
  return equation(a,b)
​
def compute(txt):
  if txt == "" :
    return txt
  if isNumber(txt):
    return float(txt)
  ops = ["=","(","/","*","+","-"]
  for op in ops:
    if txt.find(op) != -1 :
      index = txt.find(op) 
      leftTerm = txt[0:index]
      rightTerm = txt[index+1:]
      if op == "=":
        return equalsOperation(leftTerm,rightTerm)
      if op == "(":
        bracketTerm = txt[index+1:txt.find(")")]
        return compute(bracketTerm)
      if op == "/":
        if leftTerm == rightTerm:
          return 1
        return (compute(leftTerm) / compute(rightTerm))
      if op == "*":
        return (compute(leftTerm) * compute(rightTerm))
      if op == "+":
        return compute(leftTerm) + compute(rightTerm)
      if op == "-":
        return compute(leftTerm) - compute(rightTerm)
​
def formula(txt):
  txt =  txt.replace(" ","")
  if txt == "" :
    return None
  return compute(txt)

