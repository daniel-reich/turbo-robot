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

def strip_url_params(url, params_to_strip = None):
    lst_url = url.split("?")
    if len(lst_url) == 1:
        return url
    main_url = lst_url[0] + "?"
    params = lst_url[1].split("&")
​
    if params_to_strip is not None:
        for par in params:
            key = par.split("=")[0]
            if key in params_to_strip:
                params.remove(par)
​
    params_dict = {}
    for param in params:
        key = param.split("=")[0]
        params_dict[key] = param.split("=")[1]
​
    for key,value in params_dict.items():
        full_param = key +"="+ value + "&"
        main_url += full_param
​
    return main_url[:-1]

