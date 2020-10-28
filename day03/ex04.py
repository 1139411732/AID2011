# for time import sleep,ctime
import time

fi=open('my.log','a+',buffering=1)
count = 1

fi.seek(0,0)
for lien in fi:
    count+=1
while True:
    time.sleep(2)
    n=time.localtime()[:6]
    fi.write(f"{count}. {n[1]}-{n[2]}-{n[3]}  {n[3]}:{n[4]}:{n[5]}\n")
    count+=1





