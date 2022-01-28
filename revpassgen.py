import random
import string

otherStuff = "[]{}#()*;._-"

passwordlength = 15
everything = string.ascii_lowercase+string.ascii_lowercase+string.digits+otherStuff
password = "".join(random.sample(everything,passwordlength))
print("[RevPassGen] Password:", password)

input()
