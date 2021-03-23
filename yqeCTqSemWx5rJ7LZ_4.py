"""


Given a string containing a _key signature_ **written in shorthand** , create
a function which replaces the _shorthand_ with its **full written name**.

  * A **lowercase** letter denotes a **minor key**.
  * An **uppercase** letter denotes a **major key**.

See the examples below for a more helpful guide!

### Examples

    full_key_name("Prelude in C") ➞ "Prelude in C major"
    
    full_key_name("Fugue in c") ➞ "Fugue in C minor"
    
    full_key_name("Toccata and Fugue in d") ➞ "Toccata and Fugue in D minor"
    
    full_key_name("Sonata in eb") ➞ "Sonata in Eb minor"

### Notes

  * Write the _letter_ name in **uppercase** (ignore **b** and **#** ).
  * Write `"major"` or `"minor"` in all **lowercase** (rather than `"Major"` or `"Minor"`).

### Hint

The first letter of the term should always be capital, even if it's "b".

"""

def full_key_name(piece):
    temp = piece.split(' ')
    if len(temp[-1]) == 1:
        if temp[-1].isupper():
            temp.append('major')
        else:
            temp[-1] = temp[-1].upper()
            temp.append('minor')
    else:
        if temp[-1][0].isupper():
            temp.append('major')
        else:
            temp[-1] = temp[-1][0].upper()+temp[-1][1]
            temp.append('minor')
​
    return ' '.join(temp)

