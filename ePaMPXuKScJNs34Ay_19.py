"""


This challenge concerns some functionality of the `sum` method that is easy to
overlook.

As we all know, `sum([4, 14, 17, 10])` is an alternative way of writing `4 +
14 + 17 + 10`.

So far, nothing particularly interesting. However, things get more noteworthy
when one recalls that in Python the addition `+` isn't just used to add
numbers.

For example, the code:

    [1, 2] + [4] + [9, 8, 6]

... also makes perfect sense. And, as it turns out, this code can be rewritten
using `sum` as:

    sum([[1, 2], [4], [9, 8, 6]], [])

 _ **Caution:**_ One _must_ include the empty list `[]` in the code, which
tells Python "how to start the sum". More explicitly, the code above secretly
computes the sum `[] + [1, 2] + [4] + [9, 8, 6]`. Thus, if one doesn't include
`[]` then Python will try to start the sum at `0` (e.g. the code `sum([[1, 2],
[4], [9, 8, 6]])` computes `0 + [1, 2] + [4] + [9, 8, 6]`), resulting in a
type error.

Additionally, `sum` can also be used to add lists of tuples.

For example, the sum:

    (2, 4, 5) + (6,) + (9, 8, 7)

... can be similarly rewritten as:

    sum([(2, 4, 5), (6,), (9, 8, 7)], ())

 ** _Goal:_** Write a function which receives a non-empty list whose elements
are either numbers, lists, or tuples and **adds them up**. Note that in each
test all elements will be of the same type so that adding is possible.

### Examples

    add_it_up([4, 14, 17, 10]) ➞ 45
    # 4 + 14 + 17 + 10
    
    add_it_up([[1, 2], [4], [9, 8, 6]]) ➞ [1, 2, 4, 9, 8, 6]
    # [1, 2] + [4] + [9, 8, 6]
    
    add_it_up([(2, 4, 5), (6,), (9, 8, 7)]) ➞ (2, 4, 5, 6, 9, 8, 7)
    # (2, 4, 5) + (6,) + (9, 8, 7)

### Notes

  * Notably, though Python also allows us to add strings, such as with the code `"addition " + "of " + "strings"`, this addition _**can not**_ be performed using `sum`. If one attempts to run `sum(["addition ", "of ", "strings"], "")` one obtains an error message explicitly saying that `sum` does not work with strings, and indicating that one must use the alternative `"".join(["addition ", "of ", "strings"])` syntax instead.
  * If you are not familiar with tuples, you may be wondering what's the deal with the comma in the tuple `(6,)` in the third example. As it turns out, this comma is _essential_ for Python to recognize `(6,)` as a _tuple with a single entry_ , since the code `(6)` is interpreted as simply denoting the number `6`.

"""

def add_it_up(lst):
  for eachlist in lst:
    if type(eachlist) is list:
      return sum(lst,[])
    elif type(eachlist) is tuple:
      return sum(lst,())
  return sum(lst)

