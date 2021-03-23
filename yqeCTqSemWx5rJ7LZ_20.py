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
  x = piece.split(" ")
  upper = x[-1][0].isupper()
  x[-1] = x[-1].capitalize()
  if upper:
    x.append("major")
  else:
    x.append("minor")
  return " ".join(x)

