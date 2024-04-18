import sys

max = -1
maxFreq = []

for line in sys.stdin:
    word, count = line.strip().split("\t",1)
    count = int(count)
    if count>max:
        max = count
        maxFreq = [word]
    elif max == count:
        maxFreq.append(word)

for word in maxFreq:
    print(f"{word}\t{max}")