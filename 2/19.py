L = [1, 7, 19, 89, 100, 236]

result = [str(x).zfill(3) for x in L]

assert result == ['001', '007', '019', '089', '100', '236']