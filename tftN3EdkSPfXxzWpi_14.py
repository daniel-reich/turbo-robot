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

def sentence_searcher(txt, n):
  if n<0:
    n = len(txt.split())+n
  txt = [[i,len(i.split())] for i in txt.split('. ')]
  start = 0
  for a,b in txt:
    if start<=n<start+b:
      return a+'.' if a[-1]!='.' else a
    else:
      start+=b

