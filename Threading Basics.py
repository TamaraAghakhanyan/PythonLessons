#Threading -    Every process running inside an operating system
#               contains at least one thread and can further initiate
#               multiple threads, which are then executed simultaneously
#               in the same process space.
#               This is similar to executing multiple applications.
#                At the same time in Python, threading can be used to run
#                several function calls or other tasks concurrently,
#                especially if those tasks involve some waiting times.
#                 This is the case for networking applications and web
#                 related tasks, among others.

import threading
import time

# threading.Thread()
# start() - starts or initiates a thread


# join() - method makes sure the program waits for all threads to terminate.

# import time
# time.sleep() -    basically interrupts the execution of the program for
#                   as many seconds as you enter in between its parentheses.


'''def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

threads = []

for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()'''

'''Start a thread
Start a thread
Start a thread
Start a thread
Start a thread
End a threadEnd a threadEnd a thread
End a thread
End a thread'''

# without threading:
'''def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

threads = []

for i in range(5):
    myfunction()'''

'''Start a thread
End a thread
Start a thread
End a thread
Start a thread
End a thread
Start a thread
End a thread
Start a thread
End a thread'''
