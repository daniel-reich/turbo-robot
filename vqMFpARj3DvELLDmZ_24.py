"""


Write a function that removes any non-letters from a string, returning a well-
known film title.

### Examples

    letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"
    
    letters_only("^,]%4B|@56a![0{2m>b1&4i4") ➞ "Bambi"
    
    letters_only("^U)6$22>8p).") ➞ "Up"

### Notes

See the **Resources** section for more information on Python string methods.

"""

def letters_only(txt):
  return "".join(c for c in txt if ord("a")<=ord(c.lower())<=ord("z"))

