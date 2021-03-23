"""


Write a **recursive** function that will return the longest word in a
sentence. In cases where more than one word is found, return the first one.

### Examples

    find_longest("I will and ever will be gratefully and perpetually loving you Tesh!") ➞ "perpetually"
    
    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * You are expected to solve this challenge via a **recursive** approach.
  * An **iterative** versions of this challenge can be found via these links ([1](https://edabit.com/challenge/Z6kRGLpYgSuFQJ7Rx) and [2](https://edabit.com/challenge/Aw2QK8vHY7Xk8Keto)).

"""

def find_longest(s):
    n_letters = []
    longest_word = ''
​
    for i in s.split():
        n_letters.append(len(i))
​
        for j in s.split():
            if len(j) == max(n_letters):
                longest_word = j
​
        if "." in longest_word:
            longest_word = longest_word[:-1]
​
        elif "!" in longest_word:
            longest_word = longest_word[:-1]
​
        elif "'s" in longest_word:
            longest_word = longest_word[:-2]
​
        if '\"' in longest_word:
            longest_word = longest_word[1:-1]
​
    return longest_word.lower()

