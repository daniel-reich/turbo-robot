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

def next_letter(c):
    return 'a' if c == 'z' else chr(ord(c) + 1)
​
def secret_password(message):
    # step 1:
    if len(message) != 9 or not all(['a' <= c <= 'z' for c in message]):
        return "BANG! BANG! BANG!"
    # step 2:
    parts = [message[3*i:3*i+3] for i in range(3)]
    # step 3:
    parts[0] = str(ord(parts[0][0])-96) + parts[0][1] + str(ord(parts[0][2])-96)
    # step 4:
    parts[1] = parts[1][::-1]
    # step 5:
    parts[2] = ''.join([next_letter(c) for c in parts[2]])
    # step 6:
    return parts[1] + parts[2] + parts[0]

