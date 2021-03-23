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
    whitespaces = [pos for pos in range(len(txt)) if txt[pos] == " "]
    lst = [char for char in txt if char != " "]
    holder = []
    for i in range(len(lst)):
        i += n
        if i >= len(lst):
            i = i % len(lst)
        holder.append(i)
    final = list("".join([x[1] for x in sorted(list(zip(holder, lst)))]))
    for j in whitespaces:
        final.insert(j, " ")
    return("".join(final))

