import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

lines_of_code = 0

with file:
    for line in file:
        line = line.lstrip()
        if line == "" or line[0] == "#":
            continue
        lines_of_code += 1

print(lines_of_code)