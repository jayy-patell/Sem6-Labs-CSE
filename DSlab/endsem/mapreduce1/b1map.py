import fileinput

for line in fileinput.input():
    data = line.strip().split(",")
    cust_id,gender,age,annual_income,score = data
    if age == 'age': continue
    print(f'{gender}\t{age}\t{annual_income}\t')