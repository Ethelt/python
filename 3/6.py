def rectangle(w, h):
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

print(rectangle(4, 2))
