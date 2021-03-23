"""


Create a function that alternates the case of the letters in a string (known
as **Spongecase** ).

### Examples

    alternating_caps("Hello") ➞ "HeLlO"
    
    alternating_caps("How are you?") ➞ "HoW aRe YoU?"
    
    alternating_caps("OMG this website is awesome!") ➞ "OmG tHiS wEbSiTe Is AwEsOmE!"

### Notes

  * The first letter should always be UPPERCASE.
  * Ignore spaces.

"""

def alternating_caps(txt):
    b = txt.replace(" ","")
    a = list(b)
    for i in range(0,len(a)):
        if i %2==0:
            a[i] = a[i].upper()
        else:
            a[i] = a[i].lower()
    c= ''.join(a)
    d = txt.split()
    result = []
    result.append(c[0:len(d[0])])
    n=m=0
    for k in range(0,len(d)-1):
        n += len(d[k])
        result.append(c[n :n + len(d[k+1])])
    return ' '.join(result)

