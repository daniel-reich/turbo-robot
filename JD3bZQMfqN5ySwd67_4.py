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

from itertools import permutations
def is_vampire(n):
  if n<100:
    return "Normal Number"
  lst=[]
  if len(str(n))%2==0:
    lst=[int(''.join (i)) for i in list(permutations(str(n),len(str(n))//2))]
  else:
    for i in range (len(str(n))):
      lst=[]
      if i==len(str(n))-1:
        if (len(str(n))<=3):
          s1=str(n)[i:]
          s2=[str(n)[j] for j in range(len(str(n))) if j not in [i,i+1]]
        else:
          s1=str(n)[i]+str(n)[0]
          s2=[str(n)[j] for j in range(len(str(n))) if j not in [i,0]]
      else:
        s1=str(n)[i:i+len(str(n))//2]
        s2=[str(n)[j] for j in range(len(str(n))) if not j in range(i,i+len(str(n))//2)]
      s1=[s for s in s1]
      s1=(list(int(''.join(el)) for el in list(permutations(s1))))
      s2=(list(int(''.join(el)) for el in list(permutations(s2))))
      lst.append(s1)
      lst.append(s2)
      if sum([1 for i in range (len(lst[0])) for j in range (len(lst[1])) if lst[0][i]*lst[1][j]==n])>0:
        return "Pseudovampire"
    return 'Normal Number'
  cond= n in [lst[i]*lst[j] for i in range (len(lst)) for j in range (i+1,len(lst)) if lst[i]*lst[j]==n]
  return 'True Vampire' if cond and len(str(n))%2==0 else 'Normal Number'

