"""


The basic **Polybius Square** is a 5x5 square grid with the letters A-Z
written into the grid. "I" and "J" typically share a slot (as there are 26
letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
The **Bifid** cipher uses the Polybius square but adds a layer of complexity.

Start with a secret message. Remove spaces and punctuation.

    plaintext = "ikilledmufasa"

Encipher the message using the basic Polybius cipher (see my [previous
challenge](https://edabit.com/challenge/2C3gtb4treAFyWJMg) — right click and
select "open in new tab"), but write the numbers in two rows under the
message, like so:

i| k| i| l| l| e| d| m| u| f| a| s| a  
---|---|---|---|---|---|---|---|---|---|---|---|---  
2| 2| 2| 3| 3| 1| 1| 3| 4| 2| 1| 4| 1  
4| 5| 4| 1| 1| 5| 4| 2| 5| 1| 1| 3| 1  
  
Read off the numbers horizontally, in pairs:

    22 23 31 13 42 14 14 54 11 54 25 11 31

Generate the ciphertext by converting these new pairs of numbers into new
letters using the Polybius square.

    ciphertext = "ghlcrddyaykal"

Create a function that takes a plaintext or ciphertext, and returns the
corresponding ciphertext or plaintext.

### Examples

    bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"
    
    bifid("ghlcrddyaykal") ➞ "ikilledmufasa"
    
    bifid("hi") ➞ "go"

### Notes

N/A

"""

d ={'a':11,'b':12,'c':13,'d':14,'e':15,'f':21,'g':22,'h':23,'i':24,
        'j':24,'k':25,'l':31,'m':32,'n':33,'o':34,'p':35,'q':41,'r':42,
        's':43,'t':44,'u':45,'v':51,'w':52,'x':53,'y':54,'z':55}
def polybius(text):
  out= ''
  lst=[word for word in text.split()]
  if(lst[0][0].lower() in d.keys()):
    for word in lst:
      for c in word:
        if (c.isalpha()):
          out+=str(d[c.lower()])
      out+=' '
  else:
    for word in lst:
      for i in range (0,len(word),2):
        for k, v in d.items():
          if (v== int(word[i]+word[i+1])):
            if(v==24):
              if(k=='i'):
                out+=k
            else:
              out+=k
        out+=' '
  return out[:-1]
​
def bifid(text):
  a1,out=''.join(polybius(text).split()),''
  if len(a1)!= len(text)*2:
    a2 = ([(a1[k]) for k in range (len(a1)) if k%2==0],[(a1[k]) for k in range (len(a1)) if k%2==1])
    a3=(a2[0]+a2[1])
  else:
    a2 = ([(a1[k]) for k in range (len(a1)//2)],[(a1[k]) for k in range (len(a1)//2,len(a1))])
    a3=''
    for i in range (len(a2[0])):
      a3+=(a2[0][i]+a2[1][i])
  for i in range(0,len(a3),2):
    for k, v in d.items():
      if int(a3[i]+a3[i+1])==v:
        if (v==24):
          out+=('i')
          break
        else:
          out+=k
  return out

