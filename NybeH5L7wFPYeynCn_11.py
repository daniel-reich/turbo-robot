"""


Given a string, return a **sorted list** of words formed from the first three
letters, then the next three letters, shifting by only one.

### Worked Example

    three_letter_collection("edabit") ➞ ["abi", "bit", "dab", "eda"]
    # 1st word: "eda"
    # 2nd word: "dab"
    # 3rd word: "abi"
    # 4th word: "bit"
    # Remember to sort the list!

### Examples

    three_letter_collection("slap") ➞ ["lap", "sla"]
    
    three_letter_collection("click") ➞ ["cli", "ick", "lic"]
    
    three_letter_collection("cat") ➞ ["cat"]
    
    three_letter_collection("hi") ➞ []

### Notes

Return an _empty list_ if given a word with **less** than **3 letters**.

"""

def three_letter_collection(s):
    return [] if len(s) < 3 else sorted(s[i: i + 3] for i in range(len(s) - 2))

