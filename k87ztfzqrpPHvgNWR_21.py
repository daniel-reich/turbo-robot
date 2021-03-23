"""


Given a list of strings _depicting a row of buildings_ , create a function
which **sets the gap between buildings** as a given amount.

### Examples

    widen_streets([
      "###   ## #",
      "### # ## #",
      "### # ## #",
      "### # ## #",
      "### # ## #"
    ], 3) ➞
    [
      "###       ##   #",
      "###   #   ##   #",
      "###   #   ##   #",
      "###   #   ##   #",
      "###   #   ##   #"
    ]
    
    widen_streets([
      "## ### ###",
      "## ### ###",
      "## ### ###",
      "## ### ###"
    ], 2) ➞
    [
      "##  ###  ###",
      "##  ###  ###",
      "##  ###  ###",
      "##  ###  ###"
    ]
    
    widen_streets([
      "# # # # #"
    ], 2) ➞
    [
      "#  #  #  #  #"
    ]

### Notes

  * Buildings may be different sizes.
  * There will always be a starting gap size of **one character**.

"""

def widen_streets(lst, n):
    my_list = []
    final_list = []
    final_str = ""
    last = []
    for i in range (0,len(lst)):
        my_list = lst[i]
        str_list = []
        #print(my_list)
        for j in range (0,len(my_list)):
            str_list.append(my_list[j])
        #print(str_list)
        final_list = []
        for z in range (0,len(str_list)-1):
            if (str_list[z] == " " and str_list[z+1]!="#"):
                for k in range (0,n-1):
                    final_list.append(" ")
            elif (str_list[z] == " " and str_list[z+1] == "#"):
                for k in range (0,n):
                    final_list.append(" ")
            else:
                final_list.append(str_list[z])
        final_list.append("#")
        print(final_list)
        final_str = ""
        for a in range (0,len(final_list)):
            final_str+=final_list[a]
        #print(final_str)
        last.append(final_str)
    return last

