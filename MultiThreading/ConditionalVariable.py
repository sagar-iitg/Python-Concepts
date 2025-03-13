from threading import *


lock=Lock()

count=0

def task():
  
    global count
    for i in range(1000000):
        count=count+1


if __name__=='__main__':
    t1=Thread(target=task)
    t2=Thread(target=task)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count)

