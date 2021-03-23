"""


Create a function that takes a URL (string), removes duplicate query
parameters and parameters specified within the 2nd argument (which will be an
_optional_ list).

### Examples

    strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"
    
    strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"
    
    strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"

### Notes

  * The 2nd argument `params_to_strip` is optional.
  * `params_to_strip` can contain multiple params.
  * If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).

"""

def strip_url_params(url, params_to_strip=''):
  if url.endswith('.com'): return url
  
  x = url.split('?')
  y = x[1].split('&')
  temp = [i for i in y if i[0] not in params_to_strip]
  tmp_1 = [x for x in temp for y in temp
      if x[0] == y[0] and int(x[2]) > int(y[2])
                and x is not y]
  if not tmp_1:
    string = '&'.join(temp)
    return x[0] + '?' + string
  
  if tmp_1:
    lst = []
    for i in temp:
      if (i[0] == tmp_1[0][0] and
        int(i[2]) < int(tmp_1[0][2])):
        lst.append(tmp_1[0])
      elif i not in lst:
        lst.append(i)
    string = '&'.join(lst)
    return x[0] + '?' + string

