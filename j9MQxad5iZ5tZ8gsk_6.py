"""


Juan, today he learned to graph quadratic equations, so he chooses to speed up
the process and avoid having to write a lot of steps in his notebook to find
the vertex, just help him locate the vertex.

Ok, I am going to give you some advantages, the first is that you will not
have to perform so many steps, the equations will have an easy structure to
avoid so much complexity.

Here I will leave you a shorter explanation of how we can find the vertex.

We have the following equation:

    -5x ^ 2 + 50x -120

Now we apply the formula to locate the vertex:

    -b / (2 * a)

We divide our second term by 2 multiplied by the first term, remember to use
the negative sign in b. It would look like this:

    -50 / 2 * -5 = 5

... the third term will be insufficient, in the challenge but I wanted to add
it to see if it complicates you.

... remember return the result rounded to zero decimals.

### Examples

    find_vertex("-5x + 50x -120") ➞ 5
    
    find_vertex("-6x + 36x -72") ➞ 3
    
    find_vertex("7x +14x +28") ➞ -1

### Notes

List comprehension and unpacking is useful in this challenge :)

"""

def find_vertex(x):
  a, b = [int(v.replace(' ','')) for v in x.split('x')[:-1]]
  return -b // (2 * a)

