"""


Given two strings, that may or may not be of the same length, determine the
minimum number of character deletions required to make an anagram. Any
characters can be deleted from either of the strings.

### Examples

    make_anagram("cde", "abc") ➞ 4
    # Remove d and e from cde to get c.
    # Remove a and b from abc to get c.
    # It takes 4 deletions to make both strings anagrams.
    
    make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") ➞ 30
    
    make_anagram("showman", "woman") ➞ 2

### Notes

N/A

"""

def make_anagram(a, b):
  
  similarities = lambda w1, w2: [l8r for l8r in set(w1) if l8r in set(w2)]
  keep_to_sims = lambda word, sims: ''.join([l8r for l8r in word if l8r in sims])
  l8r_counts = lambda word: {l8r: word.count(l8r) for l8r in set(word)}
  l8r_cut = lambda word, adic, bdic: ''.join([l8r * min([adic[l8r], bdic[l8r]]) for l8r in set(word)])
  
  sims = similarities(a, b)
  
  a_sims = keep_to_sims(a, sims)
  b_sims = keep_to_sims(b, sims)
  
  a_lc = l8r_counts(a_sims)
  b_lc = l8r_counts(b_sims)
  
  a_cut = l8r_cut(a_sims, a_lc, b_lc)
  b_cut = l8r_cut(b_sims, a_lc, b_lc)
  
  return len(a) - len(a_cut) + len(b) - len(b_cut)

