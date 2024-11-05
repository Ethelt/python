def sum_seq(sequence):
  if len(sequence) == 0:
    return 0
  head, tail = sequence[0], sequence[1:]
  if isinstance(head, (list, tuple)):
    return sum_seq(head) + sum_seq(tail)
  return head + sum_seq(tail)

print(sum_seq([1, 2, [3, 4], [5, [6, 7]]]))
assert sum_seq([1, 2, [3, 4], [5, [6, 7]]]) == 28
