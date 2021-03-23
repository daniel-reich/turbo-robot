"""


 **Rondo Form** is a type of musical structure, in which there is a _recurring
theme/refrain_ , notated as **A**. Here are the rules for valid rondo forms:

  * Rondo forms always _start_ and _end_ with an **A** section.
  * In between the A sections, there should be contrasting sections notated as **B** , then **C** , then **D** , etc... No letter should be skipped.
  * There shouldn't be any _repeats_ in the sequence (such as ABBACCA).

Create a function which validates whether a given string is a **valid Rondo
Form**.

### Examples

    valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True
    
    valid_rondo("ABA") ➞ True
    
    valid_rondo("ABBACCA") ➞ False
    
    valid_rondo("ACAC") ➞ False
    
    valid_rondo("A") ➞ False

### Notes

  * Inputs will be given as all uppercase.
  * For the purposes of this challenge, accept **ABA** as valid Rondo forms.

"""

def valid_rondo(s):
​
  if len(s) <3:
    return False
  if s[0] == 'A' and s[-1] == 'A':
    rule1 = True
  else:
    rule1 = False
  
  rule3 = True
  alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
  
  sset = list(set(s))
  
  for item in sset:
    count = s.count(item)
    if count != 1 and item != 'A':
      rule3 = False
      break
  
  maxim = s[-2]
  end = 0
  
  for n in range(26):
    if alph[n] == maxim:
      end = n
      break
  
  should_be = []
  
  for n in range(end):
    should_be.append(alph[n])
  
  rule2 = True
  
  for l8r in should_be:
    if l8r not in s:
      rule2 = False
      break
  
  rules = [rule1, rule2, rule3]
  print(rules)
  if False in rules:
    return False
  return True

