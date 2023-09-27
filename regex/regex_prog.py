# Searching string to see if it starts with 'The' and ends with 'Germany'

import re

newtext = "The match is in German"

x = re.search("^The.*Germany$", newtext)

print(x)