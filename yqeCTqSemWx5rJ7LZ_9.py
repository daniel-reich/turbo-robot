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
  pi = piece.split()
  if pi[-1].istitle():return piece + ' major'
  else:
    pi[-1] = pi[-1].capitalize()
    return ' '.join(pi) + ' minor'

