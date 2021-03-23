"""


Character recognition software often makes mistakes when documents (especially
old ones written with a typewriter) are digitized.

Your task is to correct the errors in the digitized text. You only have to
handle the following mistakes:

  * A is misinterpreted as 4
  * S is misinterpreted as 5
  * O is misinterpreted as 0
  * I is misinterpreted as 1

The test cases contain numbers only by mistake.

### Examples

    keyboard_mistakes("MUB45H1R") ➞ "MUBASHIR"
    
    keyboard_mistakes("DUBL1N") ➞ "DUBLIN"
    
    keyboard_mistakes("51NG4P0RE") ➞ "SINGAPORE"

### Notes

N/A

"""

def keyboard_mistakes(txt):
  l=[]
  i=0
​
  l=list(txt)
​
  for i in range(len(l)):
    if l[i] == '4' :
      l[i] = "A"
    elif l[i] == '5':
      l[i] = 'S'
    elif l[i] == '0':
      l[i] = 'O'
    elif l[i] == '1':
      l[i] = 'I'
  lts=''.join(map(str,l))
​
  return lts

