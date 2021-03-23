"""


You have a dictionary with years 2015-2020 as keys and some albums released
for each year as key values. Write a function that takes an album and returns
the year in which it was released.

### Examples

    release_year("Ode to Joy") ➞ 2019
    
    release_year("Honeymoon") ➞ 2015
    
    release_year("Fake_album") ➞ "Unknown"

### Notes

  * Albums dictionary is made for you.
  * If the album isn't in the dictionary, return the string `"Unknown"`.

"""

album_dict = {
  2015: ("Vulnicura", "Honeymoon", "Rebel Heart"),
  2016: ("Lemonade", "Blackstar", "A Moon Shaped Pool"),
  2017: ("Flower Boy", "Antisocialites"),
  2018: ("El Mal Querer", "Someone Out There", "Cranberry", "Kamikaze"),
  2019: ("thank u next", "Magdalene", "Ode to Joy"),
  2020: ("Rough and Rowdy Ways", "folklore", "Future Nostalgia", "Colores")
}
​
def release_year(album):
    for key,value in album_dict.items():
        if album in value:
            return key
    return 'Unknown'

