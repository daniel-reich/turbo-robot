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

def add_next(n):
  return n + int(str(n)[::-1])
  
def is_pali(n):
  return str(n) == str(n)[::-1]
​
def lychrel(n):
  count = 0
  while not is_pali(n):
    if count == 500: return True
    n = add_next(n)
    count += 1
  return count
