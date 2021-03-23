"""


Wurst is the best. Create a function that takes a string and replaces every
mention of any type of sausage with the German word "Wurst," unless—of
course—the sausage is already a type of German "Wurst" (i.e. "Bratwurst", see
below), then leave the sausage name unchanged.

German Wursts| Convert to Wurst  
---|---  
Bratwurst| Kielbasa  
Kochwurst| Chorizo  
Leberwurst| Moronga  
Mettwurst| Salami  
Rostbratwurst| Sausage  
~| Andouille  
~| Naem  
~| Merguez  
~| Gurka  
~| Snorkers  
~| Pepperoni  
  
### Rules

  * Append sausages from the "Convert to Wurst" column with "wurst".
  * Do not replace any German sausage with the word "Wurst".
  * The word "Wurst" must be title case.

### Examples

    wurst_is_better("I like chorizos, but not sausages") ➞ "I like Wursts, but not Wursts"
    
    wurst_is_better("sich die Wurst vom Brot nehmen lassen") ➞ "sich die Wurst vom Brot nehmen lassen"
    
    wurst_is_better("Bratwurst and Rostbratwurst are sausages") ➞ "Bratwurst and Rostbratwurst are Wursts"

### Notes

All German sausage names contain the word "wurst".

"""

convert = [
    "kielbasa",
    "chorizo",
    "moronga",
    "salami",
    "sausage",
    "andouille",
    "naem",
    "merguez",
    "gurka",
    "snorkers",
    "pepperoni"
]
​
def wurst_is_better(txt):
    result = []
    for word in txt.split():
        is_plural = word[-1] == "s"
        if word.lower() in convert or is_plural and word[:-1].lower() in convert:
            result.append("Wursts" if is_plural else "Wurst")
        else:
            result.append(word)
    return " ".join(result)

