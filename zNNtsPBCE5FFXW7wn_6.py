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

#edabit
#emptying values
​
def empty_values(lst):
    result = []
    for i in lst:
        if type(i) == int:
            result.append(0)
        elif type(i) == float:
            result.append(0.0)
        elif type(i) == str:
            result.append('')
        elif type(i) == bool:
            result.append(False)
        elif type(i) == list:
            result.append([])
        elif type(i) == tuple:
            result.append(())
        elif type(i) == set:
            result.append(set())
        elif type(i) == type(None):
            result.append(None)
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

