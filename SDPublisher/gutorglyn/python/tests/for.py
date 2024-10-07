
sum = 0
lineNumbers = [1,2,3,4]

#for x in lineNumbers:
#    sum = sum + x
#print sum

#lineNumbersNew = [x%4 for x in lineNumbers]
#print lineNumbersNew


for x in lineNumbers:
    if x % 4 == 0:
        x = x
    else:
        x = ''    
    print(x)      

print type(lineNumbers)
