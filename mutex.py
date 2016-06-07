import time
from threading import Thread, Lock

def myfunc(i, mutex):
    mutex.acquire(1)
    time.sleep(1)
    print "Thread: %d" %i
    mutex.release()

def another_fun(i,mutex):
	mutex.acquire(1)
	time.sleep(0.5)
	print "Thread2: %d" %i
	mutex.release()


mutex = Lock()
for i in range(0,10):
    t = Thread(target=myfunc, args=(i,mutex))
    t2 = Thread(target=another_fun, args=(i,mutex))
    t.start()
    t2.start()
    print "main loop %d" %i