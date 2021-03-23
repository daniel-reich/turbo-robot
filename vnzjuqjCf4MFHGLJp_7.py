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
​
    result = [a for a in txt.split(' ')]
    result_n = ''.join([a for a in txt.split(' ')])
​
    for a in range(n):
        result_n = result_n[-1] + result_n[0:(len(result_n)-1)]
​
    result_n = list(result_n)
​
    for a in range(len(txt)):
       if txt[a] == ' ':
           result_n.insert(a, ' ')
​
    return ''.join([a for a in result_n])

