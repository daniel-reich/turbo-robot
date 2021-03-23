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
  def determine_spacing(line):
    
    hash_indexes = []
    
    for n in range(len(line)):
      if line[n] == '#':
        hash_indexes.append(n)
    
    difs = []
    
    for n in range(len(hash_indexes) - 1):
      difs.append(hash_indexes[n+1] - hash_indexes[n])
    
    if difs.count(difs[0]) != len(difs):
      return difs
    
    else:
      return difs[0]
      
  
  if len(hurdles) >= 4:
    return True
  
  spacing = determine_spacing(hurdles[0])
  
  if spacing < 4:
    return True
  
  return False

