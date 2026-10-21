import csv


with open("student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 20, "A"])
    writer.writerow(["Bob", 22, "B"])
    writer.writerow(["Charlie", 21, "C"])


with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)