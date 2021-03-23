"""


Write a function that returns the most frequent character in a list of words.

### Examples

    most_frequent_char(["apple", "bandage", "yodel", "make"])
    ➞ ["a", "e"]
    
    most_frequent_char(["music", "madness", "maniac", "motion"])
    ➞ ["m"]
    
    most_frequent_char(["the", "hills", "are", "alive", "with", "the", "sound", "of", "music"])
    ➞ ["e", "h", "i"]

### Notes

  * If multiple characters tie for most frequent, list all of them in alphabetical order.
  * Words will be in lower case.

"""

def most_frequent_char(lst):
    data = {}
    for word in lst:
        for char in word:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1
​
    print(data)
    count_list = data.values()
    print(count_list)
​
    max_freq = max(count_list)
    print(max_freq)
​
    answer = []
    for k,v in data.items():
        if v == max_freq:
            answer.append(k)
    answer.sort()
    return answer

