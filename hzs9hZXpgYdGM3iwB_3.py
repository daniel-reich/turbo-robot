"""


Create a function that alternates the case of the letters in a string (known
as **Spongecase** ).

### Examples

    alternating_caps("Hello") ➞ "HeLlO"
    
    alternating_caps("How are you?") ➞ "HoW aRe YoU?"
    
    alternating_caps("OMG this website is awesome!") ➞ "OmG tHiS wEbSiTe Is AwEsOmE!"

### Notes

  * The first letter should always be UPPERCASE.
  * Ignore spaces.

"""

def alternating_caps(string):
    word, index, spaces_position, space_index = list(string.lower()), 0, [], 0
    for i in word:
        if i == " ":
            spaces_position.append(space_index)
        space_index += 1
    for i in range(0,string.count(" "),1):
        word.remove(" ")
    for i in word:
        if index == 0 or index % 2 == 0:
            word[index] = i.upper()
        index+=1
    for i in spaces_position:
        word.insert(i, " ")
    return "".join(word)

