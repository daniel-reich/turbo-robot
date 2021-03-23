"""


Create a function that takes a string as an argument and tells the number of
repitions of a substring. It is exactly vice versa to repeating a string
function (i.e. if a string "k" is given and asked to make a larger string "z"
such that "k" is repated "n' times).

In this scenario, we do the opposite. Given the final string, and ask the
number of times the substring is repeated.

### Examples

    number_of_repeats("abcabcabcabc" ) ➞ 4
    
    number_of_repeats("bcbcbc") ➞ 3
    
    number_of_repeats("llbllbllbllbllbllb") ➞ 6
    
    number_of_repeats("kc") ➞ 1

### Notes

  * Assume that the substring length is always greater than 1.
  * Assume that the string length is always greater than 1.
  * Assume that the substring is not always the same.

"""

def number_of_repeats(Sample):
​
  Length = len(Sample)
  
  Multiples_A = []
  Multiples_B = []
  
  Tester = 1
  
  while (Tester <= Length):
    
    if (Length % Tester == 0):
      Number_A = Tester
      Number_B = Length / Tester
      Multiples_A.append(Number_A)
      Multiples_B.append(Number_B)
      Tester += 1
    else:
      Tester += 1
  
  Counter = 0
  Length = len(Multiples_A)
  
  while (Counter < Length):
    
    Finish = Multiples_A[Counter]
    Batch = Sample[0:Finish]
    Multiple = int(Multiples_B[Counter])
  
    if (Batch * Multiple == Sample):
      return Multiple
    else:
      Counter += 1

