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
  def get_sentence_indexes(txt):
    
    indexes = []
    
    for n in range(len(txt)):
      item = txt[n]
      if '.' in item:
        indexes.append(n)
    
    return indexes
  def convert_neg_to_pos(txt, index):
    if index >= 0:
      return index
    else:
      return len(txt) - abs(index)
  
  gsi = get_sentence_indexes(txt.split())
  cntp = convert_neg_to_pos(txt.split(), n)
  #print(gsi, cntp)
  sentences = {n: txt.split('. ')[n-1] for n in range(1, 1 + len(txt.split('. ')))}
​
  n = 1
  
  for index in gsi:
    if cntp > index:
      n += 1
  
  return sentences[n] + '.' if '.' not in sentences[n] else sentences[n]

