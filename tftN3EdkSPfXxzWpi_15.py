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
    words = txt.split()
    i = 0
    lst = []
    for word in words:
        lst += [i]
        if word[-1] == '.':
            i += 1
    sentences = txt.split('.')
    return(sentences[lst[n]].strip() + '.')

