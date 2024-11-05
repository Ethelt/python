def odwracanie(L, left, right):
  if (left < 0 or right >= len(L)):
    raise ValueError("left and right must be in range of L")
  
  while left < right:
    L[left], L[right] = L[right], L[left]
    left += 1
    right -= 1

def odwracanie_rek(L, left, right):
  if (left < 0 or right >= len(L)):
    raise ValueError("left and right must be in range of L")
  
  if left < right:
    L[left], L[right] = L[right], L[left]
    odwracanie_rek(L, left + 1, right - 1)

L = [1, 2, 3, 4, 5]
odwracanie(L, 1, 3)
print(L)
assert L ==  [1, 4, 3, 2, 5]

L = [1, 2, 3, 4, 5]
odwracanie_rek(L, 1, 3)
print(L)
assert L ==  [1, 4, 3, 2, 5]
