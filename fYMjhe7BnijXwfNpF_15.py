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
    lst = string.split(" ")
    result = ""
    for i in lst:
        if(len(i) % 2 == 0):
            result = result + i[0]
        else:
            result = result + i[int(len(i)/2)]
    return(result)

