"""


Create a function that, given a list of string lists, returns an list of all
combinations as concatenated strings.

  1. The function is called with a list of lists containing strings.
  2. The task is to combine each string of each array with each string of each other list.
  3. If one of the string lists is empty, the function will return an empty list.

The function will accept an optional second string parameter. This parameter,
if specified, is to be used to combine two strings.

### Examples

    combinator([["a", "b"], ["c", "d"]]) ➞ ["ac", "ad", "bc", "bd"]
    
    combinator([["a"], ["a", "b"], "abc"]) ➞ ["aaa", "aab", "aac", "aba", "abb", "abc"]
    
    combinator([["foo", "bar"], ["baz", "bamboo"]], " ") ➞ ["foo baz", "foo bamboo", "bar baz", "bar bamboo"]
    
    combinator([[]]) ➞ []

### Notes

  * The order of the given strings must be retained in the combinations.
  * You can assume that:
    * The function is always called with a list of string lists and lists can be empty.

"""

import itertools
def combinator(lst, sep=''):
    return [sep.join(i) for i in itertools.product(*lst)]

