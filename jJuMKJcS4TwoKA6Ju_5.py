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

dial=lambda t:t.lower().translate(t.maketrans('abcdefghijklmnopqrstuvwxyz','22233344455566677778889999'))

