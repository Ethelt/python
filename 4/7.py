def flatten(sequence):
  if not isinstance(sequence, (list, tuple)):
    return [sequence]
  
  if len(sequence) == 0:
    return []
  
  return flatten(sequence[0]) + flatten(sequence[1:])

print(flatten([1, [2, 3], [4, [5, 6]], 7]))
assert flatten([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
