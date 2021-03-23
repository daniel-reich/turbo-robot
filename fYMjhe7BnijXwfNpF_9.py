"""


Create a function that takes a string and returns the first character of every
word if the length of the word is even and the middle character if the length
of the word is odd.

### Examples

    stmid("Alexa have to paid") ➞ "ehtp"
    # "e" is the middle character of "Alexa"
    # "h" is the first character of "have"
    
    stmid("Th3 0n3 4nd 0n1y") ➞ "hnn0"
    
    stmid("who is the winner") ➞ "hihw"

### Notes

N/A

"""

def stmid(string):
 lst = string.split()
 return ''.join([lst[i][0] if len(lst[i]) % 2 == 0 else lst[i][int(len(lst[i])/2)] for i in range(len(lst))])

