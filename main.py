# Importing package
import random
# Lower case letters
lower = 'abcdefghijklmnopqrstuvwxyz'
# Upper case letters
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Symbols
symbol = '!@#$%^&*+=/-`~(){}[]?<>.,;:$_|•√π÷×§∆\}{=°^¥€¢£©®™✓[]'
# Numbers
number = '1234567890'
# Adding those strings
all = lower + upper + symbol + number
# Making length
length = 12
# Making results
password = "".join(random.sample(all, length))
# Printing First line
print("The Generated Password is : ", password)
# Printing Second line
print("Re-start the Terminal to generate another password.")
