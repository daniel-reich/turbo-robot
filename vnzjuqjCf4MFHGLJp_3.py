"""


Create a function that takes a string and shifts the letters to the right by
an amount `n` **but not the whitespace**.

### Examples

    shift_letters("Boom", 2) ➞ "omBo"
    
    shift_letters("This is a test",  4) ➞ "test Th i sisa"
    
    shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"

### Notes

  * Keep the case as it is.
  * `n` can be larger than the total number of letters.

"""

def shift_letters(txt, n):
    location = [i for i in range(len(txt)) if txt[i] == " "]
    new_txt = txt.replace(" ", "", txt.count(" "))
    n = n % len(new_txt)
    final_txt = new_txt[-n:] + new_txt[:-n]
    for i in location:
        final_txt = final_txt[:i] + " " +final_txt[i:]
    return final_txt

