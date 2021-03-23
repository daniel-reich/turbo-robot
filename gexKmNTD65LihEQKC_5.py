"""


Arun was playing random games with numbers, and he realized that four is a
number whose English reformation (i.e. FOUR, also has four letters). He
noticed an interesting pattern.

Arun starts with a few chosen strings and lands upon a number that has the
same number of letters in it as the magnitude of the number (e.g. Alienware-
Computers has nineteen letters in it, nineteen has eight letters, eight has
five and five has four letters and four again has four letters in it).

So, Alienware-Computers is a super cool string as this word can be converted
into a number which has the same length as it's magnitude when the given
string is written in English.

Arun has a few more strings. Help him figure out if they're _super cool_ or
not.

### Examples

    is_super_cool("A") ➞ True
    # "A" has one letter.
    # One has three letters.
    # Three has five letters.
    # Five has four letters.
    # Four has four letters.
    
    is_super_cool("Nura") ➞ True)
    
    is_super_cool("") ➞ False

### Notes

This challenge is _possible_ without using loops.

"""

def is_super_cool(string):
    dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
         8:'eight',9:'nine',10:'ten',11:'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
         15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
         19 : 'nineteen', 20 : 'twenty',30 : 'thirty', 40 : 'forty'}
    n=len(string)
    if n==0:
        return False
    while n:
        if n<=20:
            a=dic[n]
        if (21<n< 100):
            if n% 10 == 0:                
                a=dic[n]
            else:
                a=dic[n//10 * 10]+dic[n%10]
        if len(a)==n:
            return True
            break
        else:
            n=len(a)
    return False

