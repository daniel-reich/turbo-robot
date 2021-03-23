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
def is_contain(animal, txt):
    ls_txt = [c for c in txt]
    for c in animal:
        if c not in ls_txt:
            return False
        ls_txt.remove(c)
​
    return True
​
def possible_animals(txt):
    res = []
    for animal in animals:
        if is_contain(animal, txt):
            res.append(animal)
    return res
​
def remove_animal(txt, animal):
    ls_txt = [c for c in txt]
    for c in animal:
        ls_txt.remove(c)
    return "".join(ls_txt)
​
def count_animals(txt, num=0, max_num=0):
    for animal in possible_animals(txt):
        print(num, ":", animal)
        max_num = max(max_num, count_animals(remove_animal(txt, animal), num+1))
    max_num = max(max_num, num)
    return max_num

