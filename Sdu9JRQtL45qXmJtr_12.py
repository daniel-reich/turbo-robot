"""


 **Mubashir** is getting old but he wants to celebrate his **20th or 21st
birthday only**. It is possible with some basic maths skills. He just needs to
select the correct number base with your help!

For example, if his current age is 22, that's exactly 20 - in base 11.
Similarly, 65 is exactly 21 - in base 32 and so on.

Create a function that takes his current `age` and returns the given age **20
(or 21) years, with number base** in the format specified in the below
examples.

### Examples

    happy_birthday(22) ➞ "Mubashir is just 20, in base 11!"
    
    happy_birthday(65) ➞ "Mubashir is just 21, in base 32!"
    
    happy_birthday(83) ➞ "Mubashir is just 21, in base 41!"

### Notes

Given age will always be greater than 21.

"""

def happy_birthday(age):
  is_20 = age % 2 == 0
  base = age/2 if is_20 else (age-1)/2
  fake_age = 20 if is_20 else 21
  return "Mubashir is just " + str(fake_age) + ", in base " + str(int(base)) + "!"
