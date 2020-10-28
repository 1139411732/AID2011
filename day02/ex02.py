#!/usr/bin/python3
result = 0
list01=[]
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list01.append(i)
        result+=i
print(result)
print(list01)


#
# # result = 0
# list01=[]
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         elif i not in list01:
#             list01.append(i)
#         # result+=i
# # print(result)
# print(list01)
#
#
#