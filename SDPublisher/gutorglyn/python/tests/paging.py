import math

start = int(0)
perPage = int(40)
end = int(start + perPage)

pageValues = [0, 10, 20, 3, 40]

my_range = range(20)

print 0 + 10

print range(0, (perPage+1)*20, perPage)[1:]

pageValues1 = []
for i in range(0,20*perPage,perPage):
    pageValues1.append(i)
  
print pageValues1    

print int(math.ceil(float(36)/10))   