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

def isPalindrome(number):
    number = str(number)
    listedNum = list(number)
    listedNum = listedNum[::-1]
    reverseNum = ''.join(listedNum)
    sum = str(int(number) + int(reverseNum))
    listedSum = list(sum)
    listedSum = listedSum[::-1]
    reverseSum = ''.join(listedSum)
    if (reverseSum == sum):
        return True
    else:
        return sum
​
def lychrel(num):
    count = 0
    ans = []
    y = str(num)
    reverse = y[::-1]
    reverseStr = ''.join(reverse)
    if(y != reverseStr):
        while True:
            count = count + 1
            x = isPalindrome(y)
            y = int(x)
            if(x == True):
                break
            if (count > 500):
                count = -1
                break
            else:
                x = isPalindrome(y)
​
    if (count > -1):
        return count
    else:
        return True

