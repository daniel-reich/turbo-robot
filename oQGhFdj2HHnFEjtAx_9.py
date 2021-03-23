"""


In this challenge you are given a string and a slice made from that string.
Make a function that returns an expression that can be used to make that
slice. Your answer must contain only the minimum number of keystrokes needed
to make the slice.

### Examples

    slicer("abcd", "b") ➞ "[1]"
    
    slicer("abcdefg", "cb") ➞ "[2:0:-1]"
    
    slicer("abcdefg", "be") ➞ "[1::3]"
    
    slicer("abcdefgh", "bdf") ➞ "[1:6:2]"

### Notes

  * Test cases are slices that can be made with the `[start:end:step]` type expression.
  * The strings are composed of unique characters (no repeats).

"""

def slicer(s, slc):
    lst_idx = [s.index(c) for c in slc]
    if len(lst_idx) == 1 and len(s) > 1:
        return '[{}]'.format(lst_idx[0])
    else:
        step = lst_idx[1] - lst_idx[0]
        if step > 0:
            begin = '' if lst_idx[0] == 0 else lst_idx[0]
            end = '' if lst_idx[-1] + step >= len(s) else lst_idx[-1]
            if step == 1:
                return '[{}:{}]'.format(str(begin),
                                        str(end + 1) if end else end)
            else:
                return '[{}:{}:{}]'.format(str(begin),
                                           str(end + 1) if end else end,
                                           str(step))
        elif step < 0:
            begin = '' if lst_idx[0] == len(s) - 1 else lst_idx[0]
            end = '' if lst_idx[-1] + step < 0 else lst_idx[-1]
            return '[{}:{}:{}]'.format(str(begin),
                                       str(end - 1) if end else end,
                                       str(step))

