"""


As you know, the function `range()` returns a range of numbers, but it doesn't
work on alphabets. In this challenge, we try to fill this gap.

Write a function `alpha-range()` which takes three arguments `start`, `stop`,
and `step` (which its default value is one). The function must return a list
of alphabetical characters, ranging from start character to stop character
based on `step` value.

The function must follow these conditions:

  * If `step` is zero or more than 26 or less than -26, return `"step must be a non-zero value between -26 and 26, exclusive"`.

  * Both `start` and `stop` must share the same case, otherwise, return `"both start and stop must share the same case"`.

Like `range()` function:

  * `step` must not be zero.

Unlike `range()` function:

  * returned list must be inclusive.
  * the order of characters doesn't affect the output (i.e. the output of `alpha_range("a", "f")` is the same as `alpha_range("f", "a")`, see examples).

### Examples

    alpha_range("a", "f") ➞ ["a", "b", "c", "d", "e", "f"]
    
    alpha_range("f", "a") ➞ ["a", "b", "c", "d", "e", "f"]
    
    alpha_range("a", "f", -1) ➞ ["f", "e", "d", "c", "b", "a"]
    
    alpha_range("f", "a", -1) ➞ ["f", "e", "d", "c", "b", "a"]
    
    alpha_range("A", "F", -1) ➞ ["F", "E", "D", "C", "B", "A"]
    
    alpha_range("A", "F", 0) ➞ "step must be a non-zero value between -26 and 26, exclusive"
    
    alpha_range("A", "F", -26) ➞ "step must be a non-zero value between -26 and 26, exclusive"
    
    alpha_range("a", "F", -1) ➞ "both start and stop must share the same case"

### Notes

All the `start` and `stop` values in the tests are valid alphabetical
characters.

"""

def alpha_range(start, stop, step = 1):
  
  alph_low = 'abcdefghijklmnopqrstuvwxyz'
  alph_upp = 'abcdefghijklmnopqrstuvwxyz'.upper()
  nums = range(1, 27)
  
  alph_nums_low = {}
  alph_nums_high = {}
  nums_alph_low = {}
  nums_alph_high = {}
  
  for n in nums:
    alph_nums_low[alph_low[n-1]] = n
    alph_nums_high[alph_upp[n-1]] = n
    nums_alph_low[n] = alph_low[n-1]
    nums_alph_high[n] = alph_upp[n-1]
  
  start_case = 'L' if start.islower() == True else 'U'
  stop_case = 'L' if stop.islower() == True else 'U'
  
  if start_case != stop_case:
    return 'both start and stop must share the same case'
    
  elif start_case == 'L':
    
    start = alph_nums_low[start]
    stop = alph_nums_low[stop]
    if step > 0:
      start, stop = sorted([start, stop])
    else:
      start, stop = list(reversed(sorted([start, stop])))
      
    if step in range(-26, 27) and step != 0:
      if step > 0:
        return [nums_alph_low[n] for n in range(start, stop + 1, step)]
      else:
        return [nums_alph_low[n] for n in range(start, stop - 1, step)]
    else:
      return 'step must be a non-zero value between -26 and 26, exclusive'
  
  else:
    
    start = alph_nums_high[start]
    stop = alph_nums_high[stop]
    
    if step > 0:
      start, stop = sorted([start, stop])
    else:
      start, stop = list(reversed(sorted([start, stop])))
    
    if step in range(-26, 27) and step != 0:
      if step > 0:
        return [nums_alph_high[n] for n in range(start, stop + 1, step)]
      else:
        return [nums_alph_high[n] for n in range(start, stop - 1, step)]
    else:
      return 'step must be a non-zero value between -26 and 26, exclusive'

