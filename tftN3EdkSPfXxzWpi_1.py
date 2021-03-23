"""


Create a function that returns the sentence that contains the word at index
`n`. Remember to include the full stop at the end.

### Worked Example

    txt = "I have a dog. I have a log. There is no stopping me now."
    
    sentence_searcher(txt, 7) ➞ "I have a log."
    # The word at index 7 is "log".
    # The full sentence that contains the word at index 7 is "I have a log."
    # Return the sentence.

### Examples

    sentence_searcher(txt, 2) ➞ "I have a dog."
    
    sentence_searcher(txt, 4) ➞ "I have a log."
    
    sentence_searcher(txt, -1) ➞ "There is no stopping me now."
    # The index at -1 is the last word.
    # The last word is "now".

### Notes

  * All sentences will end with a full stop.
  * You need to also account for negative indexes.

"""

def sentence_searcher(s, n):
    lst, idx, lst_idx = s[:-1].split(". "), 0, []
    for st in lst:
        idx += len(st.split(" "))
        lst_idx.append(idx)
    n += lst_idx[-1] if n < 0 else 0
    for i, st in enumerate(lst):
        if n < lst_idx[i]:
            return "{}.".format(st)
    return "n is out of range"

