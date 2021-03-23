"""


Declare a `division()` function that gets two natural numbers (`a`, `b`) and
return a string containing the rational number `a` / `b` in the form of a
decimal fraction, possibly **periodic**.

### Examples

    division(2, 5) ➞ "0.4"
    
    division(1, 6) ➞ "0.1(6)"
    
    division(1, 3) ➞ "0.(3)"
    
    division(1, 7) ➞ "0.(142857)"
    
    division(1, 77) ➞ "0.(012987)"

### Notes

  * The length of a periodic fraction can be more than **20 numbers**.
  * The function should be efficient.

"""

def division(a, b):
  if a%b==0:
    return str(a/b)
  else:
    result = ""
    result += str(a // b)
    result += "."
    A = []
    while a:
      r = a % b
      if r == 0:
        for x in A:
          result += str(x[-1])
        break
      else:
        a = r*10
        q = a // b
        if [a, q] not in A:
          A.append([a, q])
        elif [a, q] in A:
          index = A.index([a, q])
          for x in A[:index]:
            result += str(x[-1])
          result += "("
          for y in A[index:]:
            result += str(y[-1])
          result += ")"
          break
    return result

