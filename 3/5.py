def ruler(l):
  top = ""
  bottom = ""
  top += "|"
  bottom += "0"
  for i in range(1, l + 1):
    top += "....|"
    bottom += str(i).rjust(5)
  return top + "\n" + bottom

print(ruler(12))
