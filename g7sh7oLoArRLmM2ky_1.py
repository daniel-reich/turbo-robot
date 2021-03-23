"""


This challenge makes use of a modified **Baconian** (Francis Bacon)
**cipher**. The following is an example of a (modified) Baconian ciphertext:

    ciphertext = "KNowlEDgE ITsElf Is power."

The peculiar capitalisation might, at first glance, suggest that either the
lowercase or uppercase letters contain, or code for, the hidden message (upper
= "KNEDEITEI", lower = "owlgslfspower").

But actually, the Baconian cipher is a _steganographic_ method of hiding
information. The hidden message is not in the content of the ciphertext, but
rather in the _presentation_. It doesn't matter which letters are capitalised,
just the order of the capitalisation.

To decipher the ciphertext above, remove spaces and punctuation, then cleave
the message into chunks of length 5, leaving out the remainder:

    ciphertext = "KNowl EDgEI TsElf Ispow"

Each chunk represents a letter. Decipher them according to the following table
("u" means uppercase, "l" means lowercase):

Letter| Pattern  
---|---  
a| uuuuu  
b| uuuul  
c| uuulu  
d| uuull  
e| uuluu  
f| uulul  
g| uullu  
h| uulll  
i| uluuu  
j| uluul  
k| ululu  
l| ulull  
m| ulluu  
n| ullul  
o| ulllu  
p| ullll  
q| luuuu  
r| luuul  
s| luulu  
t| luull  
u| luluu  
v| lulul  
w| lullu  
x| lulll  
y| lluuu  
z| lluul  
.| llllu  
| lllll  
      
    
    deciphered = "help"

Create a function that takes 1 or 2 arguments:

  1. A Baconian ciphertext or a plaintext message to be enciphered: `msg`.
  2. A background text in which the message is to be hidden: `mask`.

If only one argument is given (ciphertext), return the deciphered message (in
lowercase, with spaces and full stops as encoded).

If a second argument is given, encipher the first argument `msg` into the
`mask`, and return the resulting ciphertext. When enciphering, encipher full
stops and spaces along with the words. Disregard the rest. The ciphertext
itself should retain _all_ the punctuation and spaces of the original `mask`.

### Examples

    baconify("KNowlEDgE ITsElf Is power.") ➞ "help"
    
    baconify("Help me.", "Man prefers to believe what he prefers to be true.") ➞ "MAn prEFeRS To BelIeve what he PreFERS tO Be truE."
    # Both the space (between "help" and "me") and the full stop at the end are enciphered.
    
    baconify("Help!!!", "Knowledge itself is power.") ➞ "KNowlEDgE ITsElf Is power."
    # Exclamation marks not enciphered, so the resulting ciphertext is identical to the first example.

### Notes

N/A

"""

def baconify(*args):
    print(args)
    dic = {"a": "uuuuu", "b": "uuuul", "c": "uuulu", "d": "uuull", "e": "uuluu", "f": "uulul", "g": "uullu", "h": "uulll", "i": "uluuu", "j": "uluul", "k": "ululu", "l": "ulull", "m": "ulluu", "n": "ullul", "o": "ulllu", "p": "ullll", "q": "luuuu", "r": "luuul", "s": "luulu", "t": "luull", "u": "luluu", "v": "lulul", "w": "lullu", "x": "lulll", "y": "lluuu", "z": "lluul", ".": "llllu", " ": "lllll"}
    res, out = "", ""
    if len(list(args)) == 1:
        for i in args[0]:
            if i.isupper():
                res += "u"
            elif i.islower():
                res += "l"
        for i in range(len(res) // 5):
            out += list(dic.keys())[list(dic.values()).index(res[(5 * i):(5 * i) + 5])]
    elif len(list(args)) == 2:
        s = [i.lower() for i in args[0] if i not in "!?:'"]
        k = "".join([dic[i]for i in s])
        c = 0
        for i in args[1]:
            if i.isalpha() and c < len(k):
                if k[c] == "u":
                    out += i.upper()
                else:
                    out += i.lower()
                c += 1
            else:
                out += i
    return out

