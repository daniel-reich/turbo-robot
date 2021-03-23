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

from collections import Counter
def hidden_anagram(text, phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()
    text_1 = ''
    for char in text:
        if char.isalpha():
            text_1 += char.lower()
    if phrase == '':
        return ""
    if len(phrase) == 1 and phrase[0] in text:
        return phrase[0]
    elif len(phrase) == 1 and phrase[0] not in text:
        return "noutfond"
    left = 0
    right = 0
    cnt_phrase = Counter(phrase)
    while right < len(text_1):
        if text_1[right] in phrase and right - left < len(phrase) -1:
            right += 1
        elif text_1[right] in phrase and right - left == len(phrase)-1 and right < len(text_1) -1:
            cnt_result = Counter(text_1[left:right+1])
            if all(cnt_phrase[key] == cnt_result[key] for key in cnt_phrase):
                return text_1[left:right+1]
            else:
                left += 1
                right += 1
        elif text_1[right] not in phrase and right < len(text_1) - 1:
            left += 1
            right += 1
        elif text_1[right] in phrase and right - left == len(phrase)-1 and right == len(text_1) -1:
            cnt_result = Counter(text_1[left:right + 1])
            if all(cnt_phrase[key] == cnt_result[key] for key in cnt_phrase):
                return text_1[left:right + 1]
            else:
                break
        elif text_1[right] not in phrase  and right == len(text_1) - 1:
            break
    return "noutfond"

