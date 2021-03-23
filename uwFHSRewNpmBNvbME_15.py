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

vowels = ['a', 'e', 'i', 'o', 'u']
​
def same_vowel_group(w):
  
  sameVowelsWords = []
​
  firstWordVowels = get_vowels(w[0])
  for i in range(len(w)):
    newWordVowels = get_vowels(w[i])
​
    if newWordVowels == firstWordVowels:
      sameVowelsWords.append(w[i])
​
  return sameVowelsWords
​
​
​
        
def get_vowels(word):
  usedVowels = []
​
  for letter in word:
    for vowel in vowels:
      if letter == vowel and vowel not in usedVowels:
        usedVowels.append(vowel)
        
  return sorted(usedVowels)

