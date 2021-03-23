"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

def true_alphabetic(txt):
  def word_length_finder(word):
    return len(word)
  def word_maker(string, lengths):
    words = []
    string = list(string)
    for length in lengths:
      word = ''
      for n in range(length):
        word += string[0]
        string.pop(0)
      words.append(word)
    return words
  
  words = txt.split()
  word_lengths = []
  
  for word in words:
    word_lengths.append(word_length_finder(word))
  
  rawstring = sorted(''.join(words))
  string = ''
  
  for item in rawstring:
    string += item
  
  new_words = word_maker(string, word_lengths)
  
  return ' '.join(new_words)

