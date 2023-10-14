problem = input("Expression: ")
x, y, z = problem.split(" ")
match y:
    case "+":
        print(f"{float(int(x) + int(z)):.1f}")
    case "-":
        print(f"{float(int(x) - int(z)):.1f}")
    case "*":
        print(f"{float(int(x) * int(z)):.1f}")
    case "/":
        print(f"{float(int(x) / int(z)):.1f}")