"""


You have received an encrypted message from space. Your task is to decrypt the
message with the following simple rules:

  * Message string will consist of capital letters, numbers, and brackets only.
  * When there's a block of code inside the brackets, such as `[10AB]`, it means you need to repeat the letters **AB** for **10 times**.
  * Message can be embedded in multiple layers of blocks.
  * Final decrypted message will only consist of capital letters.

Create a function that takes encrypted message `txt` and returns the decrypted
message.

### Examples

    space_message("ABCD") ➞ "ABCD"
    
    space_message("AB[3CD]") ➞ "ABCDCDCD"
    # "AB" = "AB"
    # "[3CD]" = "CDCDCD"
    
    space_message("IF[2E]LG[5O]D") ➞ "IFEELGOOOOOD"

### Notes

N/A

"""

import re
def space_message(txt):
    x = re.findall(r'\[\w+\]',txt)
    if len(x) == 0:
        return txt
    num = re.findall(r'(?<=\[)\d+(?=\w+\])',txt)
    letters = re.findall(r'(?<=\d)[A-Z]+(?=\])',txt)
    subs = [j * int(i) for i,j in zip(num,letters)]
    for i in range(len(x)):
        txt = txt.replace(x[i],subs[i])
    return space_message(txt)
