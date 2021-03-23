"""


In this challenge, you have to establish if a given number is undulating. A
number `n` is undulating when the following conditions are **all true** :

  * `n` has at least three digits.
  * `n` has exactly two different digits.
  * The two digits of `n` are alternating without repeating groups.

If we think of the first digit of an undulating number as an "A", and the
second digit as a "B", we notice a sequence of the form "ABA" that can repeat
infinite times and ends either with an "A" or with a "B", but without clusters
of "AA" or "BB" in it.

Given a positive integer `n`, implement a function that returns `True` if `n`
is an Undulating number, or `False` if it's not.

### Examples

    is_undulating(121) ➞ True
    # A = 1, B = 2
    # The sequence ABA is valid
    
    is_undulating(373737) ➞ True
    # A = 3, B = 7
    # The sequence ABABABAB is valid
    
    is_undulating(12) ➞ False
    # Less than three digits
    
    is_undulating(12122) ➞ False
    # The sequence ABABB is not valid
    
    is_undulating(85856) ➞ False
    # More than two different digits

### Notes

N/A

"""

def is_undulating(n):
    if len(str(n)) < 3:
        return False
    else:
        digits = []
        for numbers in str(n):
            if numbers not in digits:
                digits.append(numbers)
        if len(digits) != 2:
            return False
        else:
            stringer = str(n)
            for i in range(len(stringer) - 1):
                if stringer[i] == stringer[i + 1]:
                    return False
                else:
                    continue
            return True

