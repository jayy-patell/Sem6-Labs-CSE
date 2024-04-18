import fileinput

for line in fileinput.input():
    data = line.strip().split("\t")
    date, time, location, item, cost, payment = data
    print(f"{location}\t{cost}")