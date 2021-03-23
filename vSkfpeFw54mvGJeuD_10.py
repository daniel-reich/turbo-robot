"""


The following is the Lychrel test.

Start with any positive number. Add the number with the number formed by
reversing its digits. Is the sum a palindrome? If not, repeat the process.

For most numbers, a palindrome is produced after a few iterations (7 or fewer)
of the process above. Numbers that never reach a palindrome are called
**_Lychrel_** numbers. No number in base 10 has been _proven_ to be a Lychrel
number, but numbers that don't produce palindromes after an unusually high
number of iterations of the reverse-and-add process are said to be **_Lychrel
candidates_**

Create a function that takes a number and returns `True` if it is a Lychrel
candidate. If it isn't, return the number of reverse-and-add iterations it
takes to produce a palindrome. For this challenge, the threshold for a Lychrel
candidate is **> =500** iterations.

### Examples

    lychrel(33) ➞ 0
    # Already a palindrome.
    
    lychrel(65) ➞ 1
    # 65+56 -> 121
    
    lychrel(348) ➞ 3
    # 348+843 -> 1191+1911 -> 3102+2013 -> 5115
    
    lychrel(295) ➞ True

### Notes

N/A

"""

def lychrel(n):
  print(n)
  for i in range(500):
    print(n)
    s = str(n)[::-1]
    print("n " + str(n) + " reversed " + s)
    print("comparing " + s[0:len(s)//2] + " with " + s[:-len(s)//2])
    if s[0:len(s)//2] == s[-len(s)//2:]:
      return i
    n = int(s) + n
    print("adding together to get " + str(n))
  return 0

