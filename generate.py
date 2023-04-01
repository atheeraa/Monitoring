import time 
from random import randrange
import threading

def xml():

    v = int(time.time())
    print(v)
    with open('data.txt','a') as out:
            s = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Data x = '"+str(v)+ "' y=\""+str(randrange(200)) +"\"/>"
            out.write(s)
            out.write('\n')
            out.close

start_time = time.time()
interval = 3
for i in range(500):
    time.sleep(start_time + i*interval - time.time())
    xml()