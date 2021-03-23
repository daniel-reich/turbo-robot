"""


Create a **recursive** function that identifies the very first item that has
recurred in the string argument passed. It returns the identified item with
the index where it **first appeared** and the very next index where it
**resurfaced** \- entirely as an object; or an empty object if the passed
argument is either `None`, an _empty_ string, or no recurring item exists.

### Examples

    recur_index("KDXTDATTDD") ➞ {"D": [1, 4]}
    // D first appeared at index 1, resurfaced at index 4
    //  though D resurfaced yet again at index 8, it's no longer significant
    // T appeared and resurfaced at indices 3 and 6 but D completed the cycle first
    
    recur_index("AKEDCBERSD") ➞ {"E": [2, 6]}
    
    recur_index("DXKETRETXD") ➞ {"E": [3, 6]}
    
    recur_index("ABCKPEPGBC") ➞ {"P": [4, 6]}
    
    recur_index("ABCDEFGHIJ") ➞ {}
    
    recur_index(None) ➞ {}

### Notes

  * There will be no exceptions to handle, all inputs are strings and string-like objects. You just need to be extra careful on `None`, and _empty_ string inputs to avoid undesirable results.
  * It is expected from the challenge-takers to come up with a solution using the concept of **recursion** or the so-called **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge or unless otherwise.
  * A non-recursive version of this challenge can be found [here](https://edabit.com/challenge/9jhTpvYgTCJyD46hA).

"""

def recur_index(txt, prev=None):
  if prev is None: prev = {}
  if not txt: return {}
  if txt[0] in prev: return {txt[0]:[prev[txt[0]],len(prev)]}
  prev[txt[0]] = len(prev)
  return recur_index(txt[1:], prev)

