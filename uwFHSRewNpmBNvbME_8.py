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
    vowel=["a","e","i","o","u"]
    vowelsfirstword=[letter for letter in w[0] if letter in vowel]
    vowelsnot=[letter for letter in vowel if letter not in vowelsfirstword]
    res=[w[0]]
    for word in w:
        for letter in word:
            if letter in vowelsfirstword and word not in res:
                res.append(word)
            elif letter in vowelsnot and word in res:
                res.remove(word)
                break
    return res

