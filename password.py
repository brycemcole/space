import string 
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
symbols = string.punctuation


def create_password(l = 18, c = lower + num) -> list:
    temp = []
    for i in range(0, l):
        temp.append(('-' if (i % 6 == 0 and i != 0) else '') + random.choice(c))
    return temp
        
# Generate a random password
# Format as 6 chars, - 6 chars, then another - and 6 chars
def build(l= 18, type=None) -> str:
    if type == None:
        temp = create_password(l)
    else: 
        c = ""
        if "upper" in type: c += upper
        if "lower" in type: c += lower
        if "symbols" in type: c += symbols
        if "numbers" in type: c += num
        temp = create_password(l, c)
    return "".join(temp)

