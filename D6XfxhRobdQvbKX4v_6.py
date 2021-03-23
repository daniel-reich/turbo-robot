"""


You are given three inputs: a string, one letter, and a second letter.

Write a function that returns `True` if every instance of the first letter
occurs **before** every instance of the second letter.

### Examples

    first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
    # Every instance of "a" occurs before every instance of "j".
    
    first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
    
    first_before_second("happy birthday", "a", "y") ➞ False
    # The "a" in "birthday" occurs after the "y" in "happy".
    
    first_before_second("precarious kangaroos", "k", "a") ➞ False

### Notes

  * All strings will be in lower case.
  * All strings will contain the first and second letters at least **once**.

"""

def first_before_second(st,w1,w2):
    s1 = []
    s2 = []
    for i in range(len(st)):
        if st[i]==w1:
            s1.append(i)
        elif st[i]==w2:
            s2.append(i)
    for a in s1:
        if a > s2[0]:
            return False
    return True

