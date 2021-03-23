"""


Create a function that takes a string as an argument and returns a coded
(h4ck3r 5p34k) version of the string.

### Examples

    hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
    
    hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
    
    hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"

### Notes

In order to work properly, the function should replace all "a"s with 4, "e"s
with 3, "i"s with 1, "o"s with 0, and "s"s with 5.

"""

def hacker_speak(txt):
  x=''
  for i in txt:
    if i.lower()=="a":
      x+='4'
    elif i.lower()=='e':
      x+='3'
    elif i.lower()=='i':
      x+='1'
    elif i.lower()=='o':
      x+='0'
    elif i.lower()=='s':
      x+='5'
    else:
      x+=str(i)
  return x

