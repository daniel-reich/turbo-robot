"""


Unfair hurdles are hurdles which are either _too high_ , or way _too close
together_.

Create a function which takes in a list of strings, representing hurdles, and
return whether they are unfair. For the purposes of this challenge, unfair
hurdles are:

  * At least **4 characters tall**.
  * Strictly less than **4 spaces** apart.

### Examples

    # Hurdle are good distance apart but are way too tall.
    
    is_unfair_hurdle([
      "#    #    #    #",
      "#    #    #    #",
      "#    #    #    #",
      "#    #    #    #"
    ]) ➞ True
    # Hurdles are a fine height but are way too close together.
    
    is_unfair_hurdle([
      "#  #  #  #",
      "#  #  #  #",
      "#  #  #  #"
    ]) ➞ True
    # These hurdles are mighty splendid.
    
    is_unfair_hurdle([
      "#      #      #      #",
      "#      #      #      #"
    ]) ➞ False

### Notes

  * Hurdles will be represented with a hashtag `"#"`.
  * There will be the same spacing between hurdles.
  * Hurdles are always as high as the length of the list.
  * Hurdles are always evenly spaced.

"""

def is_unfair_hurdle(hurdles):
  return all(len(i)<4 for i in hurdles[0].split('#')) or len(hurdles)>3

