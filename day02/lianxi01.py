result=0
for i in range(2,100001):
    for j in range(2,i//2+1):
        if i % j ==0:
            break
    else:
        result+=i
print(result)

