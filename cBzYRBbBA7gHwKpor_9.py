"""


 **Mubashir** is going on a secret mission. He needs your help but you have to
learn how to encode a secret password to communicate safely with other agents.
Create a function that takes an argument `message` and returns the **encoded
password**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    secret_password("mubashirh") ➞ "hsajsi13u2"

Step 1: Message length should be of **nine characters** containing only
lowercase letters from **'a' to 'z'**. If the argument doesn't meet this
requirement you must return `"BANG! BANG! BANG!"` (Remember, there are no
second chances in the spy world!)

Step 2: Divide the string into **three equal parts** of three characters each:

    1 - mub
    2 - ash
    3 - irh

Step 3: Convert the **first and third letter** to the corresponding number,
according to the English alphabets (ex. a = 1, b = 2, c = 3 ... z = 26, etc).

    mub = 13u2

Step 4: **Reverse** the fourth, fifth, and sixth letters:

    ash = hsa

Step 5: **Replace** seventh, eighth, and ninth letter with next letter (z will
be substituted with a).

    irh = jsi

Step 6: **Return** the string in the following order: "Part_2+Part_3+Part_1"

    "hsajsi13u2"

See the below examples for a better understanding:

### Examples

    secret_password("mubashirh") ➞ "hsajsi13u2"
    
    secret_password("mattedabi") ➞ "detbcj13a20"
    
    secret_password("HeLen-eda") ➞ "BANG! BANG! BANG!"
    # Length is not equal to 9
    # Contains characters other than lower alphabets

### Notes

N/A

"""

def secret_password(pw):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
​
    if not(pw.isalpha() and pw.islower() and len(pw) == 9):
        return "BANG! BANG! BANG!"
​
    # divide into three parts
    pw1, pw2, pw3 = pw[:3], pw[3:6], pw[6:]
​
    # convert 1st & 3rd letter of pw1 to indx # in alpha
    ch = pw1[:1]
    pre = str(alpha.index(ch) + 1 % 26)
    ch = pw1[2:]
    post = str(alpha.index(ch) + 1 % 26)
    pw1 = pre + pw[1:2] + post
​
    # reverse 4th,5th and 6th chars
    pw2 = pw2[::-1]
​
    # replace 7,8,9 with next letter in alpha
    temp = pw3[:]
    pw3 = ""
    for ch in temp:
        i = (alpha.index(ch) + 1) % 26
        pw3 += alpha[i]
​
    # return string in this order 
    return pw2+pw3+pw1

