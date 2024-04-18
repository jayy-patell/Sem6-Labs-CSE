import sys 
start_year, max_gold, max_gold_year, max_silver_year, max_silver,year_count = -1, -1,-1,-1,-1,1

for line in sys.stdin: 
    data = line.strip().split()
    year, gold, silver = data
    year,gold,silver = int(year), int(gold),int(silver)
    if start_year==-1:
        start_year,max_gold_year,max_silver_year=year,year,year
        max_gold=gold
        max_silver=silver
    elif year_count <5:
        year_count+=1
        if gold>max_gold: 
            max_gold_year=year
            max_gold = gold
        if silver>max_silver:
            max_silver_year = year
            max_silver = silver
    elif year_count==5:
        print('Gold -',max_gold_year,'-',max_gold)
        print('Silver -',max_silver_year,'-',max_silver)
        year_count=1
        max_silver=silver
        max_gold=gold
        
print('Gold -',max_gold_year,'-',max_gold)
print('Silver -',max_silver_year,'-',max_silver)