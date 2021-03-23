"""


You're able to call numbers like 1-800-flowers which replace the characters
with the associated numbers on a cellular device keyboard.

### Conversion

    abc  = 2
    def  = 3
    ghi  = 4
    jkl  = 5
    mno  = 6
    pqrs = 7
    tuv  = 8
    wxyz = 9

This is your task:

  * Create a function that takes a string as argument.
  * Convert all letters to numbers by using a cellular device keyboard as reference and leave any other characters in.
  * Return a string containing the argument with replaced letters.

### Examples

    dial("1-800-HOTLINEBLING") ➞ "1-800-468546325464"
    
    dial("abc-def-ghi-jkl!!") ➞ "222-333-444-555!!"
    
    dial("adgjmptw :)") ➞ "23456789 :)"

### Notes

  * While when you would write a SMS back in the day, to enter "b", you would have to press "2" twice. When calling numbers this is not the case as the range a-c gets converted to "2".
  * Given string can contain upper and lowercase letters.
  * Enjoy and good luck!

"""

def dial(number):
  newnumber = ""
  for letter in number.lower():
    if 'a'== letter or 'b' == letter or 'c' == letter:
      newnumber += "2"
    elif 'd'== letter or 'e' == letter or 'f' == letter:
      newnumber += "3"
    elif 'g'== letter or 'h' == letter or 'i' == letter:
      newnumber += "4"
    elif 'j'== letter or 'k' == letter or 'l' == letter:
      newnumber += "5"
    elif 'm'== letter or 'n' == letter or 'o' == letter:
      newnumber += "6"
    elif 'p'== letter or 'q' == letter or 'r' == letter or 's'== letter:
      newnumber += "7"
    elif 't' == letter or 'u' == letter or 'v'== letter :
      newnumber += "8"
    elif 'w' == letter or 'x' == letter or 'y' == letter or 'z' == letter:
      newnumber += "9"
    else:
      newnumber += letter
  return newnumber

