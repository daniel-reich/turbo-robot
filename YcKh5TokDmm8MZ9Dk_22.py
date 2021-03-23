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
    strippedText = ''.join([char.lower() for char in text if char.isalpha() is True])
    strippedPhrase = ''.join([char.lower() for char in phrase if char.isalpha() is True])
    phraseLetters = {letter: strippedPhrase.count(letter) for letter in strippedPhrase}
    for i in range(len(strippedText) - len(strippedPhrase) + 1):
        chunkLetters = {letter: strippedText[i: i + len(strippedPhrase)].count(letter) for letter in strippedText[i: i + len(strippedPhrase)]}
        if chunkLetters == phraseLetters:
            return strippedText[i: i + len(strippedPhrase)]
    else:
        return "noutfond"

