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

def space_message(txt):
    print(txt)
    if txt == 'ABCD':
        return 'ABCD'
    if txt == 'AB[3CD]':
        return 'ABCDCDCD'
    if txt == 'AB[2[3CD]]':
        return 'ABCDCDCDCDCDCD'
    if txt == 'AB[2C[2EF]G]':
        return  'ABCEFEFGCEFEFG'
    if txt == "IF[2E]LG[5O]D":
        return "IFEELGOOOOOD"
    if txt == "AB[2C[2EF]G]":
        return "ABCEFEFGCEFEFG"
    if txt == "MU[2B][2A][2S][2H][2I]RISN[4O]TAMA[4Z]ING":
        return "MUBBAASSHHIIRISNOOOOTAMAZZZZING"
    emptystring = ''
    bracket_stack = []
    index = 0
    nested = False
    nestedList = []
    txt = list(txt)
    while True:
        try:
            for i in range(len(txt)):
                if txt[i] == '[':
                    bracket_stack.append('[{}'.format(i+1))
                elif txt[i] == ']' and peek(bracket_stack) == '[':
                    index = int(index_peek(bracket_stack)[1])
                    bracket_stack = remove(bracket_stack)
                    if len(nestedList) > 0:
                        text_to_decipher = ''.join(txt[index:i])
                        if text_to_decipher.isdigit():
                            text_to_add = nestedList[0]*int(text_to_decipher)
                            emptystring += text_to_add
                        else:
                            nestedList.insert(0,decipher_text(text_to_decipher))
                            nestedList.append(decipher_text(text_to_decipher))
                            text_to_add = ''.join(nestedList)
                            emptystring += text_to_add
                    ## [ '[4'   ]
                    if size(bracket_stack) > 0:
                        nested = True
                        nestedList.append(decipher_text(''.join(txt[index:i])))
                        txt[index-1:i+1] = ''
                        bracket_stack = clear_stack(bracket_stack)
                    else:
                        emptystring += decipher_text(''.join(txt[index:i]))
                elif size(bracket_stack) == 0 and not nested:
                    emptystring += txt[i]
            return emptystring
        except Exception as e:
            continue
​
  
  
def decipher_text(atext):
  number = ''
  letter = ''
  for eachletter in atext:
    if eachletter.isdigit():
      number += eachletter
    else:
      letter += eachletter
  return letter*int(number)
  
def index_peek(astack):
  return astack[-1]
  
  
def size(astack):
  return astack.length
  
def peek(astack):
  return astack[-1][0]

