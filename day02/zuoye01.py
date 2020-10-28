result = 0
list01=[]
for i in range(2, 100001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list01.append(i)
        result+=i
print(result)
#print(list01)




