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

def secret_password(msg):
​
  #Step 1:
​
  if len([l8r for l8r in msg if l8r in 'abcdefghijklmnopqrstuvwxyz']) == len(msg) == 9:
    s1 = True
  else:
    s1 = False
  
  if s1 == False:
    return ' '.join(['BANG!'] * 3)
  
  #Step 2:
​
  part1 = msg[:3]
  part2 = msg[3:6]
  part3 = msg[6:]
​
  #Step 3:
​
  a_to_n_converter = {'abcdefghijklmnopqrstuvwxyz'[n]: n+1 for n in range(26)}
​
  part1 = list(part1)
​
  part1[0] = str(a_to_n_converter[part1[0]])
  part1[2] = str(a_to_n_converter[part1[2]])
​
  part1 = ''.join(part1)
​
  #Step 4:
​
  part2 = ''.join(list(reversed(part2)))
​
  #Step 5:
​
  alph = 'abcdefghijklmnopqrstuvwxyz'
  p3 = ''
​
  for l8r in part3:
    t = alph.index(l8r) + 1
​
    while t >= 26:
      print('l', t)
      t -= 26
    
    p3 += alph[t]
  
  part3 = p3
​
  del p3
  
  #Step 6:
​
  return part2 + part3 + part1

