"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    "A4B5C2" ➞ "AAAABBBBBCC"
    
    "C2F1E5" ➞ "CCFEEEEE"
    
    "T4S2V2" ➞ "TTTTSSVV"
    
    "A1B2C3D4" ➞ "ABBCCCDDDD"

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(txt):
  num=[]
  zimu=[]
  txt1=''
  for i in txt:
    if i in 'ABCDEFHIJKLMNOPQRSTUVWXYZ':
      zimu+=i
    else:
      num+=i
  for j in range (0,len(num)):
    txt1=txt1+zimu[j]*int(num[j])
  return txt1

