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

def strip_url_params(url, *args):
    params_to_strip = []
    for param in args:
        params_to_strip += param
    start_of_params = url.find("?")
    if start_of_params > -1:
        param_statements = get_params(start_of_params,url)
        param_dictionary = filter_params(param_statements, params_to_strip)
        url_without_params = url[0:start_of_params+1]
        for param, value in sorted(param_dictionary.items()):
            url_without_params += "" + param + "=" + value + "&"
        return url_without_params[0:-1]
    else:
        return url
​
def get_params(params_start, url):
    param_substring = url[(params_start+1)::]
    param_statements = param_substring.split("&")
    return param_statements
​
def filter_params(param_statements, params_to_strip):
    param_dictionary = {}
    for statement in param_statements:
        split_statement = statement.split("=")
        param_name = split_statement[0]
        param_value = split_statement[1]
        if param_name not in params_to_strip:
            param_dictionary[param_name] = param_value
    return param_dictionary

