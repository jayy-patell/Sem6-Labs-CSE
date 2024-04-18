import fileinput

for line in fileinput.input():
    data = line.strip().split(",")
    year,gold,silver=data
    if year=='Year': 
        continue
    print(f'{year}\t{gold}\t{silver}')