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
  n = len(s)
  return list(s) == [chr(66+i//2) if i%2 else 'A' for i in range(n)] and n%2==1 and n!=1

