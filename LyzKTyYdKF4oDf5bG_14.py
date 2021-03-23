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
    result = ""
    if " " not in s:
       result = s[:-1]
       return result
    index_space = s.find(" ")
    str_to_check = s[0:index_space]
    alpha_index = 0
    non_alpha_index = 0
    for i in range(len(str_to_check)):
        if str_to_check[i].isalpha():
            alpha_index = i
            break
    if all(str_to_check[i].isalpha() for i in range(len(str_to_check))):
          non_alpha_index = -1
    else:
        for j in range(len(str_to_check)):
            if not str_to_check[j].isalpha():
                non_alpha_index = j
                break
​
    if alpha_index < non_alpha_index:
        result = str_to_check[0:non_alpha_index].lower()
    elif alpha_index > non_alpha_index and non_alpha_index != -1:
        for i in range(alpha_index, len(str_to_check)):
            if not str_to_check[i].isalpha():
                result = str_to_check[alpha_index:i].lower()
                break
    elif alpha_index > non_alpha_index and non_alpha_index == -1:
        result = str_to_check.lower()
    return result if len(result) >= len(find_longest(s[index_space + 1:])) else find_longest(s[index_space+1:])

