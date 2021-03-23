"""


In **Digital Cipher** , encoding is done by the simple addition of numbers in
the key and the corresponding characters on a string input.

Create a function that takes two arguments; a positive integer and a string
and returns an encoded list of integers as message.

Assign a unique number to each letter of the alphabet.

     a  b  c  d  e  f  g  h  i  j  k  l  m
     1  2  3  4  5  6  7  8  9  10 11 12 13
     n  o  p  q  r  s  t  u  v  w  x  y  z
     14 15 16 17 18 19 20 21 22 23 24 25 26

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "scout"
    key = 1939
    
    digital_cipher(message, key) ➞ [20, 12, 18, 30, 21]

Write the corresponding number against each character:

     s  c  o  u  t
    19  3 15 21 20

Add to each obtained digit consecutive digits from the key:

       s  c  o  u  t
      19  3 15 21 20
     + 1  9  3  9  1
     ---------------
      20 12 18 30 21

See the below example for a better understanding:

    message = "masterpiece"
    key = 1939
    
    digital_cipher(message, key) ➞ [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
    
       m  a  s  t  e  r  p  i  e  c  e
      13  1 19 20  5 18 16  9  5  3  5
    +  1  9  3  9  1  9  3  9  1  9  3
      --------------------------------
      14 10 22 29  6 27 19 18  6  12 8

### Examples

    digital_cipher("scout", 1939) ➞ [20, 12, 18, 30, 21]
    
    digital_cipher("mubashir", 1990) ➞ [14, 30, 11, 1, 20, 17, 18, 18]
    
    digital_cipher("edabit", 100) ➞ [6, 4, 1, 3, 9, 20]

### Notes

Liked this challenge ? Let's decode your encrypted version
[here](https://edabit.com/challenge/pyDemMDspSSFdWsh4)!!!

"""

def digital_cipher(message, key):
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16,
               'q': 17, 'r': 18, 's': 19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24,  'y':25,  'z':26}
    result = []
    key = list(str(key))
​
    for i in range(len(message)):
        element = my_dict[message[i]] + int(key[i % len(key)])
        result.append(element)
    return result

