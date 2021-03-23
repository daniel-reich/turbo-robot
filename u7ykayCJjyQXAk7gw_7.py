"""


 **Mubashir** needs your help to find out **number of animals** hidden in a
given string `txt`.

You are provided with an array of animals given below:

    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
    "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
    "frog", "hen", "mole", "duck", "goat"]

 **Rule:** Return the **maximum number** of animal names. See the below
example:

    txt = "goatcode"
    
    count_animals(txt) ➞ 2
    # First animal = "dog"
    # Remaining string = "atcoe",
    # Second animal = "cat".
    # count = 2 (correct)
    
    # If you got a "goat" first time
    # remaining string = "code",
    # no animal will be found during next time.
    # count = 1 (wrong)

### Examples

    count_animals("goatcode") ➞ 2
    # "dog", "cat"
    
    count_animals("cockdogwdufrbir") ➞ 4
    # "cow", "duck", "frog", "bird"
    
    count_animals("dogdogdogdogdog") ➞ 5

### Notes

N/A

"""

animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def get_letter_counts(txt):
    cnt = [0] * 26
    for c in txt:
        cnt[ord(c) - 97] += 1
    return cnt
​
def dfs(animal_counts, txt_count, ans):
    answers = [ans]
    for animal in animals:
        if all([animal_counts[animal][i] <= txt_count[i] for i in range(26)]):
            new_txt_count = txt_count[:]
            for i in range(26):
                new_txt_count[i] -= animal_counts[animal][i]
            answers.append(dfs(animal_counts, new_txt_count, ans + 1))
    return max(answers)
    
def count_animals(txt):
    animal_counts = {a: get_letter_counts(a) for a in animals}
    txt_count = get_letter_counts(txt)
    return dfs(animal_counts, txt_count, 0)

