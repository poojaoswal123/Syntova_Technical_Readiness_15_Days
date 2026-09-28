# STRINGS
# indexing
name = "Pooja"
print(name[0])
print(name[-1])

# slicing
text = "Python"
print(text[0:3])

# string methods
text = "  Python Programming  "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(text.split())
print(text.count("m"))
print(text.count("Python"))
print(text.startswith("  Python"))
print(text.endswith("Programming  "))
print(text.find("Python"))
print(text.swapcase())
print(text.title())

words = ["Python", "Programming", "Language"]
print(" ".join(words))
print(", ".join(words))

sentence = "Python is powerfull . Python is easy."
print(sentence.split())

t = "Python"
print(t.isidentifier())  # letter and num are allow but should start with letter only not number

num = "12345"
print(num.isnumeric()) # there should be only num no letters

p = "Python\nProgramming"
print(p.isprintable()) # \n is not allowed only letetrs and num

mixed_text = "Python123"
print(mixed_text.isalnum()) # only letter and num are allowed ( no space or special char is allowed)

sample = "Python"
print(sample.isalpha()) # checks whether the string contains only letters and no numbers and space are allowed

sample = "Python 123"
print(sample.isascii()) # isascii() checks whether all characters belong to the ASCII character set.


number_text = "12345"
print(number_text.isdecimal())# isdecimal() checks whether all characters are decimal digits (0–9).here point is not allowed

number_text = "12345"
print(number_text.isdigit())# isdigit() checks whether all characters are digits.

# alpha    → A-Z / a-z
# num      → 0-9
# alnum    → alpha + number
# ascii    → ASCII characters
# decimal  → decimal digits
# digit    → digits

