"""


Write a function that connects each previous word to the next word by the
shared letters. Return the resulting string (removing **duplicate characters**
in the overlap) and the **minimum** number of shared letters across all pairs
of strings.

### Examples

    join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", 2]
    
    join(["move", "over", "very"]) ➞ ["movery", 3]
    
    join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]
    
    # "to" and "ops" share "o" (1)
    # "ops" and "psy" share "ps" (2)
    # "psy" and "syllable" share "sy" (2)
    # the minimum overlap is 1
    
    join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", 0]

### Notes

More specifically, look at the overlap between the previous words **ending
letters** and the next word's **beginning letters**.

"""

def join(lst: list):
    result, shared_letters = lst[0], []
    paired_list = list(zip(lst, lst[1:]))
    for pair in paired_list:
        word1, word2 = pair[0], pair[1]
        last_letter = word1[-1]
        for i, letter in enumerate(word2):
            if letter not in word1:  # add letter if it is not found in word1
                result += letter
            elif letter in word1 and letter == last_letter:  # add the remainder slice of the word
                result += word2[i + 1:]
                shared_letters.append(i + 1)
                break
    return [result, min(shared_letters) if shared_letters else 0]

