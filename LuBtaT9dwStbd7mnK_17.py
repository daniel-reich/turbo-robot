"""


Given a list of strings (depicting a skyline of _several buildings_ ), return
_in meters_ the **height of the tallest building**. _Each line_ in the list
represents **20m**.

### Examples

    tallest_building_height([
      "            ##",
      "            ##",
      "            ##",
      "###   ###   ##",
      "###   ###   ###",
      "###   ###   ###",
      "###   ###   ###"
    ]) ➞ "140m"
    
    # Tallest building is 7 characters
    # 7 x 20m = 140m
    
    tallest_building_height([
      "               ",
      "               ",
      "               ",
      "       #    ###",
      "      # #   ###",
      "###   ###   ###",
      "###   ###   ###"
    ]) ➞ "80m"
    
    # Tallest building is 4 characters
    # 4 x 20m = 80m
    
    tallest_building_height([
      "                              ",
      "                         ###  ",
      "                         ###  ",
      "###                    #####  ",
      "###      #             #####  ",
      "###     ###            #####  ",
      "######  ###            #######",
      "######  ######  ###    #######",
      "###################    #######",
      "###############################",
      "###############################"
    ]) ➞ "200m"
    
    # Tallest building is 10 characters
    # 10 x 20m = 200m

### Notes

  * There may be some **open sky** above buildings (can't _just_ find the length of the list).
  * There may be multiple tallest buildings (see example #2).

"""

def tallest_building_height(lst):
   x = len([i for i in lst if "#" in i]) * 20
   return str(x) + "m"

