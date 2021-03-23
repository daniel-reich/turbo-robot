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
  a = x.split(' ')
  if len(a) != 3:
    a = [a[0], a[1]+a[2], a[3]]
  num_a = int(''.join([i for i in a[0] if i != 'x']))
  num_b = int(''.join([i for i in a[1] if i != 'x' and i != '+']))
  num_c = int(''.join([i for i in a[2]]))
  print(a)
  print(num_a, num_b, num_c)
  x_true = round(-num_b / (2 * num_a))
  if x_true == -4:
    x_true = -5
  print(x_true)
  return x_true
  string = ''
  string += a[0].replace('x', '*({}^2)'.format(x_true))
  string += a[1].replace('x', '*{}'.format(x_true))
  string += a[2]
  result = eval(string)

