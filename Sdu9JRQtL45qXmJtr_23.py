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

import string
​
def happy_birthday(age):
    base_twenty = 0
    base_twenty_one = 0
    incrementer = 3
    ### test 20
    while base_twenty < age:
        base_twenty = int_to_base(20,incrementer)
        incrementer += 1
    if base_twenty == age:
        return 'Mubashir is just 20, in base {}!'.format(incrementer-1)
    incrementer = 3
    while base_twenty_one < age:
        base_twenty_one = int_to_base(21,incrementer)
        incrementer += 1
    if base_twenty_one == age:
        return 'Mubashir is just 21, in base {}!'.format(incrementer-1)
        
def int_to_base(num,base):
    total = 0
    str_number = str(num)
    power_increment = 1
    for eachletter in str_number:
        total += int(eachletter) * base**power_increment
        power_increment -= 1
    return total

