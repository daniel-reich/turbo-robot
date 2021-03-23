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

def baconify(msg, *mask):
    code='uuuuu-uuuul-uuulu-uuull-uuluu-uulul-uullu-uulll-uluuu-uluul-ululu-ulull-ulluu-ullul-ulllu-'
    code+='ullll-luuuu-luuul-luulu-luull-luluu-lulul-lullu-lulll-lluuu-lluul-llllu-lllll'
    punc=',:;?.! '
    if mask==():
        for i in punc:
            msg=msg.replace(i,'')
        p=0
        new=''
        for i in msg:
            if i.isalpha():
                p+=1
                if p%5==0:
                    new+=msg[p-5:p]+' '
        new=new.split()
        ans=''
        for i in new:
            dec=''
            for j in i:
                if j.isupper():
                    dec+='u'
                else:
                    dec+='l'
            x=chr(code.find(dec)//6+97)
            if x=='{':x='.'
            if x=='|':x=' '
            ans+=x
        return ans
    else:
        p=0
        msg=msg.lower()
        mask=str(mask[0]).lower()
        for i in msg:
            dec=6*(ord(i)-97)
            cw=code[dec:dec+5]
            if i=='.':cw='llllu'
            if i==' ':cw='lllll'
            for j in cw:
                m=mask[p]
                while m in punc:
                    p+=1
                    m=mask[p]
                if j=='u':
                    mask=mask[:p]+m.upper()+mask[p+1:]
                p+=1
    return mask

