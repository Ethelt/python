while True:
    user_input = input()
    if user_input == "stop":
        break
    
    try:
        x = float(user_input)
        print(x**3)
    except ValueError:
        print("Proszę podać liczbę lub stop")
