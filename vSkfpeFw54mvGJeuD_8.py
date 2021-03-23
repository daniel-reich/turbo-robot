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

def lychrel(num):
    i = 0
    while i < 500:
        num2 = str(num)[::-1]
        if str(num) == num2:
            return i
            break
        else:
            s = int(num) + int(num2)
            if str(s) == str(s)[::-1]:
                i+=1
                return i
                break
            else:
                num = s
                i+=1
                continue
    else:
        return True

