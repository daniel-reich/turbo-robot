"""


Given a list of values, return a list with each value replaced with the _empty
value_ of the same type.

More explicitly:

  * Replace integers (e.g. `1, 3`), whose type is `int`, with `0`
  * Replace floats (e.g. `3.14, 2.17`), whose type is `float`, with `0.0`
  * Replace strings (e.g. `"abcde", "x"`), whose type is `str`, with `""`
  * Replace booleans (`True, False`), whose type is `bool`, with `False`
  * Replace lists (e.g. `[1, "a", 5], [[4]]`), whose type is `list`, with `[]`
  * Replace tuples (e.g. `(1,9,0), (2,)`), whose type is `tuple`, with `()`
  * Replace sets (e.g. `{0,"a"}, {"b"}`), whose type is `set`, with `set()`
    * Caution: Python interprets `{}` as the _empty dictionary_ , **not** the empty set.
  * `None`, whose type is `NoneType`, is preserved as `None`

### Examples

    empty_values([1, 2, 3]) ➞ [0, 0, 0]
    
    empty_values([7, 3.14, "cat"]) ➞ [0, 0.0, ""]
    
    empty_values([[1, 2, 3], (1,2,3), {1,2,3}]) ➞ [[], (), set()]
    
    empty_values([[7, 3.14, "cat"]]) ➞ [[]]
    
    empty_values([None]) ➞ [None]

### Notes

`None` has the special `NoneType` all for itself.

"""

def empty_values(lst):
  return type(lambda: 0)(type((lambda: 0).__code__)(1, 0, 3, 4, 67, b'g\x00}\x01x\xe8|\x00D\x00]\xe0}\x02t\x00|\x02\x83\x01t\x01k\x08r&|\x01j\x02d\x01\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x03k\x08r>|\x01j\x02d\x02\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x04k\x08rV|\x01j\x02d\x03\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x05k\x08rn|\x01j\x02d\x04\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x06k\x08r\x86|\x01j\x02g\x00\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x07k\x08r\x9e|\x01j\x02f\x00\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x08k\x08r\xb8|\x01j\x02t\x08\x83\x00\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\tk\x08r\xd0|\x01j\x02i\x00\x83\x01\x01\x00q\nt\x00|\x02\x83\x01t\x00d\x00\x83\x01k\x08r\n|\x01j\x02d\x00\x83\x01\x01\x00q\nW\x00|\x01S\x00', (None, 0, 0.0, '', False), (), ('l', 'r', 'i'), '', '', 79, b'\x00\x01\x04\x01\n\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x0e\x01\x0c\x01\x0c\x01\x10\x01\x0e\x01', (), ()), {})(lst)

