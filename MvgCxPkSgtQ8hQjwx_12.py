"""


Create a function that takes a string and returns a new string with all vowels
removed.

### Examples

    remove_vowels("I have never seen a thin person drinking Diet Coke.")
    ➞ " hv nvr sn  thn prsn drnkng Dt Ck."
    
    remove_vowels("We're gonna build a wall!")
    ➞ "W'r gnn bld  wll!"
    
    remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
    ➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"

### Notes

  * "y" is not considered a vowel.
  * Expect a valid string for all test cases.

"""

def remove_vowels(txt):
  
  Step01 = txt.replace("A","")
  Step02 = Step01.replace("E","")
  Step03 = Step02.replace("I","")
  Step04 = Step03.replace("O","")
  Step05 = Step04.replace("U","")
  Step06 = Step05.replace("a","")
  Step07 = Step06.replace("e","")
  Step08 = Step07.replace("i","")
  Step09 = Step08.replace("o","")
  Step10 = Step09.replace("u","")
  
  return Step10

