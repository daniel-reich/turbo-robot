"""


 **Mubashir** needs your help to learn Python Programming. Help him by
modifying a given string `txt` as follows:

  * Reverse the string given.
  * Replace each letter to its position in the alphabet for example (a = 1, b = 2, c = 3, ...).
  * Join the array and convert it to a number.
  * Convert the number to binary.
  * Convert the string back to a number.

See below example for more understanding :

 **modify("hello") ➞ 111001101011101101101010**

     "hello" = "olleh"
     
     "olleh" = ['15', '12', '12', '5', '8']
     
     ['15', '12', '12', '5', '8'] = 15121258
     
     15121258 = "111001101011101101101010"
     
     "111001101011101101101010" = 111001101011101101101010

### Examples

    modify("hello") ➞ 111001101011101101101010
    
    modify("mubashir") ➞ 10110000110010000110011111000111000001
    
    modify("edabit") ➞ 111111110110001110001

### Notes

There are no spaces and the string is lowercase.

"""

def modify(astr):
    return convert_binary_to_number(convert_number_to_binary(join_array_and_convert_to_number(replaceLetterWithAlpha(reverse(astr)))))
​
​
​
​
​
​
​
def reverse(astr):
    return astr[::-1]
​
​
def replaceLetterWithAlpha(astr):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    newlist = []
    astr = astr.lower()
    for eachletter in astr:
        newlist.append(str((alphabet.index(eachletter))))
    return newlist
​
​
def join_array_and_convert_to_number(alist):
    emptystring = ''.join(alist)
    return int(emptystring)
​
def convert_number_to_binary(anumber):
    return bin(anumber)[2:]
​
def convert_binary_to_number(binarynumber):
    return int(binarynumber)

