import re

txt = "The rain in spain"

# x = re.sub("spain", "germany", txt)

x = re.sub("\s", "Y", txt, 1)

print(x)