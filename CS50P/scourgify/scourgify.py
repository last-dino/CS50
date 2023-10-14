import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    in_file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

students = []
with in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        last, first = row["name"].split(", ")
        students.append({"first" : first, "last" : last, "house" : row["house"]})

with open(sys.argv[2], "w") as out_file:
    writer = csv.DictWriter(out_file, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)