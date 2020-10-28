# with open('ling.txt','w+') as l:
#     l.write('hello kitty\n')
#     data=l.read()
#     print(data)
#

f = open('ling.txt', 'w', buffering=1)
# f = open('ling.txt', 'wb', buffering=10)
# f=open('ling.txt','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    # f.write(data.encode())
    f.fileno()
    item =f.read()
    print(item)