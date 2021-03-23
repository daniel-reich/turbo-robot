"""


Create a function that takes two strings. The first string contains a sentence
containing the letters of the second string in a consecutive sequence but in a
different order. The hidden anagram must contain all the letters, including
duplicates, from the second string in any order and must not contain any other
alphabetic characters.

Write a function to find the anagram of the second string embedded somewhere
in the first string. You should ignore character case, any spaces, and
punctuation marks and return the anagram as a lower case string with no spaces
or punctuation marks.

### Examples

    hidden_anagram("An old west action hero actor", "Clint Eastwood") ➞ "noldwestactio"
    # The sequence "n old west actio" is a perfect anagram of "Clint Eastwood".
    
    hidden_anagram("Mr. Mojo Rising could be a song title", "Jim Morrison") ➞ "mrmojorisin"
    # The sequence "Mr. Mojo Risin" ignoring the full stop, is a perfect
    # anagram of "Jim Morrison".
    
    hidden_anagram("Banana? margaritas", "ANAGRAM") ➞ "anamarg"
    # The sequence "ana? marg" ignoring "?" is a perfect anagram of "Anagram".
    
    hidden_anagram("D  e b90it->?$ (c)a r...d,,#~", "bad credit") ➞ "debitcard"
    # When all spaces, numbers and puntuation marks are removed
    # from the whole phrase, the remaining characters form the sequence
    # "Debitcard" which is a perfect anagram of "bad credit".
    
    hidden_anagram("Bright is the moon", "Bongo mirth") ➞ "noutfond"
    # The words "Bright moon" are an anagram of "bongo mirth" but they are
    # not a continuous alphabetical sequence because the words "is the" are in
    # between. Hence the negative result, "noutfond" is returned.

### Notes

  * A perfect anagram contains all the letters of the original, in any order, no more, no less.
  * If there is no hidden anagram in the sentence, return `"noutfond"`.
  * As in the above examples, the hidden anagram may start or finish part way through a word and/or span multiple words and may contain punctuation marks and other non-alpha characters.
  * Ignore character case and any embedded non-alpha characters.
  * If there is more than 1 result in a sentence, return the nearest to the beginning.

"""

def hidden_anagram(text, phrase):
  
  class Word:
    
    def find_anagrams(word):
      from itertools import permutations as p
      
      perms = list(p(word, len(word)))
      return [''.join(perm) for perm in perms]
    
    def __init__(self, word):
      self.word = word.lower().replace(' ', '')
  #   self.anagrams = Word.find_anagrams(self.word)
      self.l8r_counts = {}
      for l8r in set(self.word):
        count = self.word.count(l8r)
        self.l8r_counts[l8r] = count
    
    def __len__(self):
      return len(self.word)
    
    def is_anagram(self, phrase):
      for l8r in set(phrase):
        if l8r not in self.l8r_counts.keys():
          return False
        else:
          count = phrase.count(l8r)
          if count != self.l8r_counts[l8r]:
            return False
      return True
  
  
  class Sentence:
    
    def __init__(self, sentence):
      self.sentence = sentence.lower().replace(' ', '')
      valid = 'abcdefghijklmnopqrstuvwxyz'
      
      for item in self.sentence:
        if item not in valid:
          self.sentence = self.sentence.replace(item, '')
          
    def find_anagram(self, word):
      anagram_length = len(word)
      
      poss_anagrams = []
      
      for n in range(len(self.sentence)):
        try:
          s = self.sentence[n:n+anagram_length]
        except IndexError:
          s = self.sentence[n:]
        
        if len(s) < anagram_length:
          break
        else:
          poss_anagrams.append(s)
      
      for anagram in poss_anagrams:
        if word.is_anagram(anagram) == True:
          return anagram
      
      return 'noutfond'
      
  phrase = Word(phrase)
  sentence = Sentence(text)
  
  return sentence.find_anagram(phrase)

