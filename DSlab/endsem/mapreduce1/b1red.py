import fileinput

gender = None
age = 0
max_sal = 0
min_sal = 0

for line in fileinput.input():
    data = line.strip().split("\t")

    curr_age, curr_gender, curr_sal = data
    
    if gender == None:
        gender = curr_gender
        age = curr_age
        max_sal = int(curr_sal)
        min_sal = int(curr_sal)
        continue
    if curr_gender == gender and curr_age == age:
        if int(curr_sal) > max_sal :
            max_sal = int(curr_sal)
        if int(curr_sal) < min_sal:
            min_sal = int(curr_sal)
    else:
        print(age,"\t",gender,"\t",max_sal,"\t",min_sal)
        age = curr_age
        gender = curr_gender
        max_sal = int(curr_sal)
        min_sal = int(curr_sal)

if curr_gender == gender and curr_age == age :
    print(age,"\t",gender,"\t",max_sal,"\t",min_sal)