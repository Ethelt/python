line = "lorem ipsum dolor sit amet"

firsts = [word[0] for word in line.split()]
lasts = [word[-1] for word in line.split()]

assert firsts == ['l', 'i', 'd', 's', 'a']
assert lasts == ['m', 'm', 'r', 't', 't']