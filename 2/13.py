line = "lorem ipsum dolor sit amet"

result = sum([len(word) for word in line.split()])

assert result == 22