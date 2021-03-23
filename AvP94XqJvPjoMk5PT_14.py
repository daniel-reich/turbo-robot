"""


There are many different styles of music and many albums exhibit multiple
styles. Create a function that takes a **list** of musical styles from albums
and returns how many styles are **unique**.

### Examples

    unique_styles([
      "Dub,Dancehall",
      "Industrial,Heavy Metal",
      "Techno,Dubstep",
      "Synth-pop,Euro-Disco",
      "Industrial,Techno,Minimal"
    ]) ➞ 9
    
    unique_styles([
      "Soul",
      "House,Folk",
      "Trance,Downtempo,Big Beat,House",
      "Deep House",
      "Soul"
    ]) ➞ 7

### Notes

N/A

"""

def unique_styles(my_list):
    tmp_list = []
    for i in my_list:
        tmp = i.split(",")
        for j in tmp:
            tmp_list.append(j)
    return len(set(tmp_list))

