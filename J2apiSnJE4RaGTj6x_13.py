"""


Given what is supposed to be typed and what is actually typed, write a
function that returns the broken key(s). The function looks like:

    find_broken_keys(correct phrase, what you actually typed)

### Examples

    find_broken_keys("happy birthday", "hawwy birthday") ➞ ["p"]
    
    find_broken_keys("starry night", "starrq light") ➞ ["y", "n"]
    
    find_broken_keys("beethoven", "affthoif5") ➞ ["b", "e", "v", "n"]

### Notes

  * Broken keys should be ordered by when they first appear in the sentence.
  * Only one broken key per letter should be listed.
  * Letters will all be in lower case.

"""

def find_broken_keys(txt1, txt2):
    array = []
​
    l1 = list(txt1)
    l2 = list(txt2)
​
    for i in range(len(l1)):
        if l2[i] != l1[i]:
            array.append(l1[i])
​
    answer = []
    for i in array:
        if i not in answer:
            answer.append(i)
​
    return answer

