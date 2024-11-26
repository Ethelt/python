import itertools
import random

# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
iter_a = itertools.cycle([0, 1])
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
iter_b = iter(lambda: random.choice(["N", "E", "S", "W"]), -1)
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]. 
iter_c = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

print("a:")
for i in range(10):
    print(next(iter_a))

print("b:")
for i in range(10):
    print(next(iter_b))

print("c:")
for i in range(10):
    print(next(iter_c))