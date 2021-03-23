"""


Write a function that changes every letter to the next letter:

  * "a" becomes "b"
  * "b" becomes "c"
  * "d" becomes "e"
  * and so on ...

### Examples

    move("hello") ➞ "ifmmp"
    
    move("bye") ➞ "czf"
    
    move("welcome") ➞ "xfmdpnf"

### Notes

There will be no z's in the tests.

"""

def move(word):
    x=[('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),('g','h'),('h','i'),('i','j'),('j','k'),('k','l'),('l','m'),('m','n'),('n','o'),('o','p'),('p','q'),('q','r'),('r','s'),('s','t'),('t','u'),('u','v'),('v','w'),('w','x'),('x','y'),('y','z')]
    y=[]
    for i in word:
        for j,k in x:
            if i==j:
                y.append(k)
    return ''.join(y)

