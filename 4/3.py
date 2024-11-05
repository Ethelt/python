def factorial(n):
  if (n < 0):
    raise ValueError("n must be non-negative")
  result = 1
  for x in range(1, n + 1):
    result *= x
  return result

print(factorial(5))
assert factorial(5) == 120
assert factorial(0) == 1
