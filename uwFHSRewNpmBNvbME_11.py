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

def same_vowel_group(arr):
    vowels = ['a','e','i','o','u']
    vowelsInFirst = []
    countOfFirst = 0
    result = []
​
    for i in arr[0]:
        if (i in vowels) and (i not in vowelsInFirst):
            vowelsInFirst.append(i)
            countOfFirst += 1
    # print(vowelsInFirst,countOfFirst)
    for i in arr:
        temp = 0
        tempVowel = []
        for j in i:
            if (j in vowels) and (j not in tempVowel):
                tempVowel.append(j)
                temp += 1
        if (temp == countOfFirst) and (sorted(tempVowel) == sorted(vowelsInFirst)):
            # print("asdfgh",sorted(tempVowel), sorted(vowelsInFirst))
            result.append(i)
        # print("Temp",tempVowel,temp)
​
    return result

