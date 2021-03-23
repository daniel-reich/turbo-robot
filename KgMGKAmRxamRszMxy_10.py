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

class Spartan:
  
  def __init__(self, slides):
    self.slides = slides
  
  def encode(self, msg):
    if msg == '':
      return msg
    slide_size = len(msg) // self.slides if len(msg) % self.slides == 0 else len(msg) // self.slides + 1
    
    slides = [[] for slide in range(slide_size)]
    #print(slides, 'slides')
    for n in range(len(msg)):
      try:
        slides[n].append(msg[n])
      except IndexError:
        #print(slides, n, slide_size, n%slide_size)
        slides[n%slide_size].append(msg[n])
    
    slides = [''.join(slide) for slide in slides]
    ns = []
    for slide in slides:
      #print(slide, len(slide), self.slides)
      while len(slide) < self.slides:
        slide += ' '
        #print(slide, len(slide), 'L.24')
      ns.append(slide)
    
    
    tr = ''.join(ns)
    
    while tr[0] == ' ':
      tr = tr[1:]
    while tr[-1] == ' ':
      tr = tr[:-1]
    
    return tr
    
def spartans_cipher(message, n_Slide):
  
  msg = Spartan(n_Slide)
  m = msg.encode(message)
  
  return m

