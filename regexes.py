import re

exampleString = """
Jessica is 15 years old, Daniel is 27 years old.
Edward is 97, his grandfather, Oscar, is 102.
"""

# findall takes regex as first arg, target string as second
ages = re.findall(r"\d{1,3}", exampleString)

names = re.findall(r"[A-Z][a-z]*", exampleString)

print(ages)
print(names)
