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
    vowels={"a","e","i","o","u"}
    l=[]
    s=set(w[0])
    k=s&vowels
    for i in range(0,len(w)):
        if k==set(w[i])&vowels:
            l.append(w[i])
    return l

