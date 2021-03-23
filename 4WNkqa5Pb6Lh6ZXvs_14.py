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
  def expression_formatter(poly, num):
    
    np = ''
    tt = False
    for n in range(0, len(poly)):
      item = poly[n]
      try:
        titem = poly[n + 1]
      except IndexError:
        titem = None
      
      if titem == 'x':
        try:
          i = int(item)
          np += item + '*x'
          tt = True
        except ValueError:
          np += item
      elif item == 'x':
        if tt == False and n != len(poly) - 1:
          try:
            nitem = int(poly[n + 1])
            np += 'x*'
          except ValueError:
            np += 'x'
        if tt == True:
          tt = False
      else:
        np += item
    poly = np
    del tt, np
    expression = poly.replace('x', str(num))
    
​
    formatted = ''
    open_brackets = 0
    closed_brackets = 0
​
    for n in range(0, len(expression)):
      operators = '+ - * ^ / %'.split()
      item = expression[n]
      try:
        t = int(item)
        formatted += item
      except ValueError:
        if item == '(':
          open_brackets += 1
          titem = expression[n - 1]
          try:
            t = int(titem)
            formatted += '*{i}'.format(i = item)
          except ValueError:
            formatted += '{i}'.format(i = item)
        elif item == ')':
          closed_brackets += 1
          formatted += item
        elif item not in operators:
          return False, item
        else:
          formatted += item
    
    if open_brackets != closed_brackets:
      return False
    
    if open_brackets > 0:
      parenthesis = True
    else:
      parenthesis = False
​
    return formatted, parenthesis
  def math_problem(data):
    def solution(problem):
      n1 = None
      n2 = None
      operator = None
​
      for n in range(0, len(problem)):
        item = problem[n]
        try:
          i = int(item)
          if operator == None:
            if n1 == None:
              n1 = i
            else:
              n1 = int(str(n1) + str(i))
          else:  
            if n2 == None:
              n2 = i
            else:
              n2 = int(str(n2) + str(i))
        except ValueError:
          if operator == None:
            operator = item
          else:
            if operator == '*' and item == '*':
              operator += item
      
      
      if operator == '+':
        return n1 + n2
      elif operator == '-':
        return n1 - n2
      elif operator == '*':
        return n1 * n2
      elif operator == '/':
        return n1 / n2
      elif operator == '%':
        return n1 % n2
      elif operator == '^':
        return n1 ** n2
      else:
        return False, n1, n2   
    
    expression = data[0]
    parenthesis = data[1]
​
    while parenthesis == True:
​
      inparenthesis = {}
​
      ip_key_ranges = []
      current_key_range = []
​
      for n in range(0,len(expression)):
        item = expression[n]
        if item == '(':
          current_key_range = [n]
        elif item == ')':
          current_key_range.append(n + 1)
          ip_key_ranges.append(current_key_range)
          current_key_range = []
      
      del current_key_range
​
      ip_keys = []
​
      for key_range in ip_key_ranges:
        start = int(key_range[0])
        end = int(key_range[1])
​
        key = ''
        for n in range(start, end):
          key += expression[n]
        ip_keys.append(key)
      
      for key in ip_keys:
        expres = key.strip('(').strip(')')
        val = solution(expres)
        inparenthesis[key] = val
      
      for key in ip_keys:
        
        expression = expression.replace(key, str(inparenthesis[key]))
      
      parenthesis = False
​
    #exponents
​
    for n in range(0, len(expression)):
      try:
        item = expression[n]
      except IndexError:
        break
      
      if item == '^':
        
        n1s = ''
​
        for num in reversed(range(0, n)):
          try:
            n1s += str(int(expression[num]))
          except ValueError:
            break
        
        n1l = list(reversed(n1s))
        n1s = ''
        for item in n1l:
          n1s += item
        n1 = int(n1s)
        
        n2s = ''
        for num in range(n + 1, len(expression)):
          try:
            n2s += str(int(expression[num]))
          except ValueError:
            break
        n2 = int(n2s)
        
        problem = '{n1}^{n2}'.format(n1 = n1, n2 = n2)
        s = solution(problem)
​
        expression = expression.replace(problem, str(s))
    
    #multiplication / division
​
    mds = '* /'.split()
​
    for n in range(0, len(expression)):
      try:
        item = expression[n]
      except IndexError:
        break    
      if item in mds:
        operator = item
        n1l = []
        for num in reversed(range(0, n)):
          try:
            i = int(expression[num])
            n1l.append(i)
          except ValueError:
            break
        n1l = reversed(n1l)
        n1s = ''
        for item in n1l:
          n1s += str(item)
        n1 = int(n1s)
        
        n2s = ''
        for num in range(n + 1, len(expression)):
          try:
            i = int(expression[num])
            n2s += str(i)
          except ValueError:
            break
        try:
          n2 = int(n2s)
        except ValueError:
          return 'invalid'      
        problem = '{n1}{i}{n2}'.format(n1 = n1, i = operator, n2 = n2)
        s = solution(problem)
        
        expression = expression.replace(problem, str(s))
​
    #addition/subtraction
​
    ads = '+ -'.split()
​
    for n in range(0, len(expression)):
      try:
        item = expression[n]
      except IndexError:
        return expression
​
      if item in ads:
        operator = item
        
        n1l = []
        for num in reversed(range(0, n)):
          try:
            t = int(expression[num])
            n1l.append(t)
          except ValueError:
            break
        n1l = reversed(n1l)
        n1s = ''
        for item in n1l:
          n1s += str(item)
        n1 = int(n1s)
​
        n2s = ''
        for num in range(n + 1, len(expression)):
          try:
            t = int(expression[num])
            n2s += str(t)
          except ValueError:
            break
        n2 = int(n2s)
​
        problem = '{n1}{o}{n2}'.format(n1 = n1, o = operator, n2 = n2)
        s = solution(problem)
​
        expression = expression.replace(problem, str(s))
    
    return expression
  
  if 'x' not in poly:
    return 'invalid'
  
  expression = expression_formatter(poly, num)
​
  if expression[0] == False:
    return 'invalid'
  
  m = math_problem(expression)
  try:
    return int(float(m))
  except ValueError:
    return m

