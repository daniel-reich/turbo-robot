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

def eval_bracket(txt):
    cnt = ""
    while '0' <= txt[0] <= '9':
        cnt += txt[0]
        txt = txt[1:]
    return txt * int(cnt)
​
def space_message(txt):
    if ']' not in txt:
        return txt
    idx2 = txt.find(']')
    idx1 = idx2 - 1
    while idx1 > 0 and txt[idx1] != '[':
        idx1 -= 1
    txt = txt[:idx1] + eval_bracket(txt[idx1+1:idx2]) + txt[idx2+1:]
    return space_message(txt)

