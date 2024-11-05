def fibonacci(n):
  if (n < 1):
    raise ValueError("n must be positive")
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a

print(fibonacci(10))
assert fibonacci(10) == 55
