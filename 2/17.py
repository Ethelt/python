line = "lore ipsums dolor sit"

words = line.split()

by_alphabet = sorted(words)

by_length = sorted(words, key=len)

assert by_alphabet == ['dolor', 'ipsums', 'lore', 'sit']
assert by_length == ['sit', 'lore', 'dolor', 'ipsums']
