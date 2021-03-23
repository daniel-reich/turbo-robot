"""


A Vampire Number is a positive integer greater than 99, that rearranged in all
of its possible digits permutations, with every permutation being split into
two parts, is equal to the product of at least one of its permutations.

  * If the number has an even quantity of digits, left and right parts will have the same length in every permutation;
  * If the number has an odd quantity of digits and at least three digits, the left and right parts will present different lengths for every possible permutation, alternating between them in the range +1 and -1.

Given a positive integer `n`, implement a function that returns the type of
`n` as a string:

  * `'Normal Number'` if `n` is lower than 100 or if no permutations return a product of their parts equal to `n`.
  * `'Pseudovampire'` if `n` it is a Vampire with an odd quantity of digits.
  * `'True Vampire'` if `n` it is a Vampire with an even quantity of digits.

### Examples

    is_vampire(1260) ➞ "True Vampire"
    # Has an even number of digits and is greater than 99)
    # Permutations:
    # 12 * 60 = 720
    # 16 * 20 = 320
    # 10 * 26 = 260
    # 21 * 60 = 1260
    
    is_vampire(126) ➞ "Pseudovampire"
    # Has an odd number of digits and is greater than 99
    # Permutations:
    # 12 * 6 = 72
    # 1 * 26 = 26
    # 21 * 6 = 126
    
    is_vampire(67) ➞ "Normal Number"
    # Is lower than 100
    # Permutations:
    # 6 * 7 = 7 * 6 = 42

### Notes

Trivially, a number from 1 to 99 is a Normal Number by the definitions: a
single-digit number can't be split into two parts, and the product of the
permutated two digits of a number will always be lower than the number itself.

"""

def is_vampire(n):
  def even_perms(perms):
    
    half = int(len(perms[0]) / 2)
    
    permutations = []
​
    for perm in perms:
      p1l = perm[:half]
      p2l = perm[half:]
​
      p1s = ''
      for n in p1l:
        p1s += str(n)
      p2s = ''
      for n in p2l:
        p2s += str(n)
​
      p1 = int(p1s)
      p2 = int(p2s)
​
      if len(list(str(p1))) != len(list(str(p2))):
        continue
​
      permutation_combo = [p1, p2]
​
      if permutation_combo not in permutations:
        permutations.append(permutation_combo)
​
    return permutations 
​
    return p1, p2
  def odd_perms(perms):
​
    half = int(len(perms[0]) / 2)
    half1 = half + 1
​
    biggest = True
    tr = []
​
    for perm in perms:
      
      n1l = perm[:half1]
      n2l = perm[half1:]
​
      n1s = ''
      for item in n1l:
        n1s += str(item)
      n2s = ''
      for item in n2l:
        n2s += str(item)
​
      n1 = int(n1s)
      n2 = int(n2s)
​
      if len(list(str(n1))) - 1 != len(list(str(n2))):
        return 'ERROR L232'
      else:
        tr.append([n1, n2])
      
      n1l = perm[:half]
      n2l = perm[half:]
​
      n1s = ''
      for item in n1l:
        n1s += str(item)
      n2s = ''
      for item in n2l:
        n2s += str(item)
​
      n1 = int(n1s)
      n2 = int(n2s)
​
      if len(list(str(n2))) - 1 != len(list(str(n1))):
        return 'ERROR L251'
      else:
        tr.append([n1, n2])
​
    return tr
  def multi_test(perms, n):
​
    answer = False
​
    for pair in perms:
​
      n1 = int(pair[0])
      n2 = int(pair[1])
​
      product = n1 * n2
​
      if product == n:
        answer = True
        break
    
    return answer
​
  import itertools as i
  l = list(str(n))
  nl = []
  for item in l:
    nl.append(int(item))
  l = nl
  del nl
​
  permutations = list(i.permutations(l))
​
  if n <= 99:
    return 'Normal Number'
  
  even = False
  if len(list(str(n))) % 2 == 0:
    even = True
  
  if even == True:
    perms = even_perms(permutations)
  else:
    perms = odd_perms(permutations)
​
  answer = multi_test(perms, n)
​
  if answer == False:
    return 'Normal Number'
  else:
    if even == True:
      return 'True Vampire'
    else:
      return 'Pseudovampire'

