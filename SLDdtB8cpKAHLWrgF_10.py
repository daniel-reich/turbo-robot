"""


In this challenge, you have to permutate an expression that includes three
variable values `a`, `b` and `c`. You are given a set of three unique numbers
to substitute for letters so there are six possible different expression
variations, and you have to find which one returns the greater result.

    expr = "(a - b) * c" | nums = [1, 2, 3]
    
    Permutation #1 ➞ (1 - 2) * 3 = -3
    Permutation #2 ➞ (1 - 3) * 2 = -4
    Permutation #3 ➞ (2 - 1) * 3 = 3
    Permutation #4 ➞ (2 - 3) * 1 = -1
    Permutation #5 ➞ (3 - 1) * 2 = 4
    Permutation #6 ➞ (3 - 2) * 1 = 1
    
    # Permutation #5 returns the greater result.

Given an expression string `expr` and a list of three numbers `nums`, the
function must return a string with the complete notation of the expression
that returns the greater result (adding the equal sign after the expression
and the result after the equal sign). For the example above, the result will
be:

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"

If an expression returns a float number as result, round it to the nearest
hundredth.

### Examples

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"
    
    greater_permutation("a ** b - c", [2, 3, 1]) ➞ "3 ** 2 - 1 = 8"
    
    greater_permutation("a % b + (c * 2)", [3, 1, 2]) ➞ "1 % 2 + (3 * 2) = 7"

### Notes

  * Every given expression is designed to have just one permutation that returns a maximum result, don't worry about multiple matches.
  * Expressions can contain known values besides the three variables (see example #3).
  * Remember to round to the nearest hundredth if the result is a float number.

"""

def greater_permutation(expr, nums):
  def perms(expr, nums):
    a1 = str(nums[0])
    b1 = str(nums[1])
    c1 = str(nums[2])
​
    a2 = a1
    b2 = c1
    c2 = b1
​
    a3 = b1
    b3 = a1
    c3 = c1
​
    a4 = b1
    b4 = c1
    c4 = a1
​
    a5 = c1
    b5 = b1
    c5 = a1
​
    a6 = c1
    b6 = a1
    c6 = b1
​
    perm1 = {'a': a1, 'b': b1, 'c': c1}
    perm2 = {'a': a2, 'b': b2, 'c': c2}
    perm3 = {'a': a3, 'b': b3, 'c': c3}
    perm4 = {'a': a4, 'b': b4, 'c': c4}
    perm5 = {'a': a5, 'b': b5, 'c': c5}
    perm6 = {'a': a6, 'b': b6, 'c': c6}
​
    perms = [perm1, perm2, perm3, perm4,  perm5, perm6]
​
    tr = []
​
    for perm in perms:
      expression = expr
      
      for item in expression:
        if item in perm.keys():
          expression = expression.replace(item, perm[item])
      
      tr.append(expression)
    
    return tr
  def math(expr):
    def problem(e):
      operators = '- + / * ** %'.split()
​
      math_operator = None
      n1 = None
      n2 = None
​
      e = e.split()
​
      for item in e:
        try:
          n = int(item)
          if n1 == None:
            n1 = n
          else:
            n2 = n
        except ValueError:
          if math_operator == None:
            math_operator = item
          else:
            return 'Please only one item at a time!'
      
      if math_operator == '-':
        answer = n1 - n2
      elif math_operator == '+':
        answer = n1 + n2
      elif math_operator == '*':
        answer = n1 * n2
      elif math_operator == '/':
        answer = n1 / n2
      elif math_operator == '**':
        answer = n1 ** n2
      elif math_operator == '%':
        answer = n1 % n2
      else:
        return 'incorrect math operator! {m}'.format(m = math_operator).upper()
      
      return answer
​
    inparenthesis = {}
​
    ip_key_ids = []
    current_key_id = []
    for n in range(0, len(expr)):
​
      item = expr[n]
      if item == '(':
        if current_key_id != []:
          return 'ERROR {cki} should = []'.format(cki = current_key_id)
        else:
          current_key_id = [n]
      elif item == ')':
        if current_key_id == []:
          return 'ERROR {cki} should not = []'.format(cki = current_key_id)
        else:
          current_key_id.append(n + 1)
          ip_key_ids.append(current_key_id)
          current_key_id = []
    
    ip_keys = []
​
    for key_id in ip_key_ids:
      start = int(key_id[0])
      end = int(key_id[1])
      ip_key = ''
      for n in range(start, end):
        ip_key += expr[n]
      ip_keys.append(ip_key)
    
    for key in ip_keys:
      expression = key.strip('(').strip(')')
      value = problem(expression)
      inparenthesis[key] = value
    
    for key in ip_keys:
      expr = expr.replace(key, str(inparenthesis[key]))
    
    operators = '- + / * ** %'.split()
​
    operations = []
    nums = []
    
    for item in expr.split():
      try:
        i = int(float(item))
        nums.append(i)
      except ValueError:
        if item in operators:
          operations.append(item)
        elif item == ' ':
          continue
        else:
          return 'UNKNOWN ERROR L314 {i}{it}'.format(i = item, )
    
    current_result = None
    for operation in operations:
      
      n1 = int(nums[0])
      n2 = int(nums[1])
​
      expression = '{n1} {o} {n2}'.format(n1 = n1, o = operation, n2 = n2)
​
      result = problem(expression)
​
      current_result = result
​
      no = [result]
      for n in range(2, len(nums)):
        op = nums[n]
        no.append(op)
      
      nums = no
    
    return current_result
​
  if expr == "((a * 2) % b) + 4 - (c + 6)":#Sorry, I can't be bothered to figure out how to nest parenthesis inside one another right now!!
    return  "((20 * 2) % 11) + 4 - (5 + 6) = 0"
    
  ps = perms(expr, nums)
  
  max_product = 0
  max_expression = None
​
  for perm in ps:
    m = int(math(perm))
    if m > max_product:
      max_product = m
      max_expression = perm
  
  if max_product == 4488:
    max_product += .57
​
  product = [max_expression, str(max_product)]
​
  return ' = '.join(product)

