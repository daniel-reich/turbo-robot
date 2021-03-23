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
  vowelpresent = []
  vowels = ["a","e","i","o","u"]
  res = []
  for i in w[0]:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      if i not in vowelpresent: vowelpresent.append(i)
      if i in vowels: vowels.remove(i)
  for i in w:
    flag=0
    for j in vowelpresent:
      if j not in i:
        flag=1
        break
    for k in i:
      if k in vowels:
        flag=1
        break
    if flag==0: res.append(i)
  return res

