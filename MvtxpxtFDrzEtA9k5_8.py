"""


A number may not be a palindrome, but its descendant can be. A number's direct
child is created by summing each pair of adjacent digits to create the digits
of the next number.

For instance, `123312` is not a palindrome, but its next child `363` is,
where: `3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2`.

Create a function that returns `True` if the **number itself** is a palindrome
or any of its **descendants down to 2 digits** (a 1-digit number is trivially
a palindrome).

### Examples

    palindrome_descendant(11211230) ➞ True
    # 11211230 ➞ 2333 ➞ 56 ➞ 11
    
    palindrome_descendant(13001120) ➞ True
    # 13001120 ➞ 4022 ➞ 44
    
    palindrome_descendant(23336014) ➞ True
    # 23336014 ➞ 5665
    
    palindrome_descendant(11) ➞ True
    # Number itself is a palindrome

### Notes

Numbers will always have an even number of digits.

"""

def palindrome_descendant(num):
    num=str(num)
    even=[]
    odd=[]
    total=[]
    string=[]
    if len(num)%2!=0:
        return False
    else:
        if num==num[::-1]:
            return True
        else:
            for i in range(len(num)):
                if i%2==0:
                    even.append(int(num[i]))
                else:
                    odd.append(int(num[i]))
            for i in range(len(even)):
                total.append(even[i]+odd[i])
            for i in range(len(total)):
                string.append(str(total[i]))
            o=''.join(string)
            #print(o)
            if len(o)>1 and len(o)%2==0:
                if o==o[::-1]:
                    return True
                else:
                    return palindrome_descendant(int(o))
            else:
                return False

