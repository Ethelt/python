line = "The authors are GvR and John Lock"

result = line.replace("GvR", "Guido van Rossum")

assert result == "The authors are Guido van Rossum and John Lock"