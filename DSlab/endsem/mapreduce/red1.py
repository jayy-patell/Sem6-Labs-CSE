import sys
last_word = None
sum = 0
for line in sys.stdin:
     word,count= line.strip().split("\t",1)
     count = int(count)
     if last_word == None:
          last_word = word
          sum = count
          continue
     if  word == last_word:
          sum += count
     else:
          print(f"{last_word}\t{sum}")
          sum = count
          last_word = word

if last_word == word:
    print( '%s\t%s' % (last_word, sum ) )

          
          



