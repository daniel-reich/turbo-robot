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
  n=len(message)//n_Slide
  if (len(message)%n_Slide)!=0:
    n+=1
  s=''
  for i in range(n):
    for j in range(n_Slide):
      if j*n+i<len(message):
        s+=message[j*n+i]
      elif (j*n+i)<(n*(n_Slide)):
        s+=" "
  return s.rstrip()

