def make_ruler(l):
  top = ""
  bottom = ""
  top += "|"
  bottom += "0"
  for i in range(1, l + 1):
    top += "....|"
    bottom += str(i).rjust(5)
  return top + "\n" + bottom

print(make_ruler(12))

def make_grid(w, h):
  rect = ""
  for y in range(h):
    for x in range(w):
      rect += "+---"
    rect += "+\n"
    for x in range(w):
      rect += "|   "
    rect += "|\n"
  for x in range(w):
    rect += "+---"
  rect += "+"
  return rect

print("\n\n\n")
print(make_grid(4, 2))

