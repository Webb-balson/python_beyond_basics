import re

txt = "The rain in spain"

x = re.search("\s", txt)

print(x.end())