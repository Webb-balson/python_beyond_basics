import re

txt = "The rain in spain"

x = re.search("ai", txt)

print(x)

print(x.span())
print(x.string)
print(x.group())