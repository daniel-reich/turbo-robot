"""


Write a function that returns the first `n` vowels of a string.

### Examples

    first_n_vowels("sharpening skills", 3) ➞ "aei"
    
    first_n_vowels("major league", 5) ➞ "aoeau"
    
    first_n_vowels("hostess", 5) ➞ "invalid"

### Notes

  * Return `"invalid"` if the `n` exceeds the number of vowels in a string.
  * Vowels are: _a, e, i, o, u_

"""

def first_n_vowels(txt, n):
    vowels = ["a", "e", "i", "o", "u"]
    ret = []
    j = 0
    s = ""
​
    for i in txt:
        # print(i)
        if j < n:
            #   print("inside 2")
            if i in vowels:
                #   print("inside")
                ret.append(i)
                j += 1
    if len(ret) < n:
        return "invalid"
    else:
        return s.join(ret)

