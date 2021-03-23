"""


Given a sentence, return the number of words which have the **same first and
last letter**.

### Examples

    count_same_ends("Pop! goes the balloon") ➞ 1
    
    count_same_ends("And the crowd goes wild!") ➞ 0
    
    count_same_ends("No I am not in a gang.") ➞ 1

### Notes

  * Don't count single character words (such as "I" and "A" in example #3).
  * The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
  * Mind the punctuation!
  * Bonus points indeed for using regex!

"""

def count_same_ends(txt):
  def validator(word):
    return len(word) > 1
  def correction(word):
    correct = ''
    incorrect = list('!.,;@!%^')
    
    for l8r in word:
      if l8r not in incorrect:
        correct += l8r
    
    return correct
  def compare(word):
    return word[0].lower() == word[-1].lower()
  
  words = txt.split()
  valid = []
  
  for word in words:
    if validator(word) == True:
      valid.append(word)
  
  correct = []
  
  for word in valid:
    correct.append(correction(word))
  
  count = 0
  
  for word in correct:
    if compare(word) == True:
      count += 1
  
  return count

