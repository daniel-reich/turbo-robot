"""


Write a function that selects all words that have all the same vowels (in any
order and/or number) as the first word, including the first word.

### Examples

    same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
    
    same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]
    
    same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]

### Notes

  * Words will contain only **lowercase letters** , and **may contain whitespaces**.
  * Frequency **does not** matter (e.g. if the first word is "loopy", then you can include words with any number of o's, so long as they **only** contain o's, and not any other vowels).

"""

def same_vowel_group(w):
  def calc_val(word):
      vowels = {"a":1, "e":2, "i":4, "o":8, "u":16}
      out = 0
      for letter in word:
          out = out | vowels.get(letter, 0)
          #bitwise or to get unique outputs based on vowels
      return out
​
  out = [w[0],]
  target = calc_val(w[0])
  for word in w[1:]:
      if calc_val(word) == target:
          out.append(word)
  return out

