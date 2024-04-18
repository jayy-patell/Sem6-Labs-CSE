import sys

sum = 0.0
total_count = 0
for line in sys.stdin:
    city, total = line.strip().split("\t",1) 
    total = float(total)

    sum += total
    total_count += 1

print(f"{total_count}\t{sum}") 
