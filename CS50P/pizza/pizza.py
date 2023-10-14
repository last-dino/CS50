import sys
import csv
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

table = []
with file:
    reader = (csv.reader(file))
    for row in reader:
        table.append(row)

print(tabulate.tabulate(table, headers="firstrow", tablefmt="grid"))