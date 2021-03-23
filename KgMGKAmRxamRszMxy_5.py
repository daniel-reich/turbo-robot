"""


In **Spartans Cipher** , encoding is done by writing the text horizontally,
across the strap in the plaintext word of a message. In ancient times,
Spartans and Greeks invented an interesting way of encryption called
[Scytale](https://en.wikipedia.org/wiki/Scytale).

The ancient Greeks, and the Spartans in particular, are said to have used this
cipher to communicate during military campaigns.

Create a function that takes two arguments, a number of slides `n_Slide` and a
string `message`, and returns the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "Mubashir Scytale Code"
    n_Slide = 6
    
    spartans_cipher(message, n_Slide) ➞ "Ms t euhSaC biclo aryed"

 **Step 1:** Imagine this Scytale:

![S](https://edabit-challenges.s3.amazonaws.com/199px-Skytale.png)

 **Step 2:** You can write the given message on a **6 slide** Scytale like
this:

    | M | u | b | a |
    | s | h | i | r |
    |   | S | c | y |
    | t | a | l | e |
    |   | C | o | d |
    | e |   |   |   |

 **Step 3:** Encode the message **column-wise** :

    "Ms t euhSaC biclo aryed "

 **Step 4:** Trim **all spaces at the end** and return the final encoded
message:

    "Ms t euhSaC biclo aryed"

See the below examples for a better understanding:

### Examples

    spartans_cipher("Mubashir Scytale Code", 6) ➞ "Ms t euhSaC biclo aryed"
    
    spartans_cipher("Matt and Edabit are amazing", 8) ➞ "M  baai aaEirmn tndteag tda  z"
    
    spartans_cipher("", 99) ➞ ""

### Notes

N/A

"""

def spartans_cipher(message, n_Slide):
  
  if not message:
    return ""
  arr = [] 
  
  if len(message) % n_Slide == 0:
    horizontal_length = int(len(message) / n_Slide)
  else:
    horizontal_length = len(message) // n_Slide + 1
  
  while message:
    
    temp_holder = [] 
    for i in range(horizontal_length): 
      try:
        temp_holder.append(message[0])
        message = message[1:]
        flag = False
      except Exception as e:
        # Index error 
        # The string is empty 
        temp_holder.append(" ")
        flag = True 
        break
    arr.append(temp_holder)
    if flag and len(arr) != n_Slide: 
      arr.append([" " for i in range(horizontal_length)])
  
  while len(arr[-1]) != horizontal_length:
    arr[-1].append(" ")
    
​
  for i in arr: print(i)
​
  encoded = "" 
  for i in range(horizontal_length):
    for row in arr:
      encoded += row[i]
  
  print()
  print(encoded)
  return(encoded.rstrip())

