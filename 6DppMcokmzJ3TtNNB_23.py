"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

def true_alphabetic(txt):
    lens = [len(i) for i in txt.split()]
    all_sorted = sorted(j for i in txt.split() for j in i)
    n = 0
    final = []
    for i in range(len(lens)): # 0, 1, 2
        final.append((str("".join(all_sorted[n : n + lens[i]])))) 
        n = n + lens[i]
    return " ".join(final)

