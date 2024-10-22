line = "lorem ipsums dolor sit amet"

longest = max(line.split(), key=len)

assert longest == 'ipsums'

longest_length = len(longest)

assert longest_length == 6