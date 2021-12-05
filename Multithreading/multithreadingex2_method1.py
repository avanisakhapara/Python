import threading
import time

def listen(n1): #4
    for i in range(n1):#i-> 0 to 3
        time.sleep(4)
        print(f"Finished listening to {i+1} session")

def eat(n2):
    for i in range(n2):
        time.sleep(5)
        print(f"Finished eating breakfast fooditem {i+1}")

def drink(n3):
    for i in range(n3):
        time.sleep(3)
        print(f"Finished drinking tea/coffee {i+1} time")

#method1 - using callable object
t1=threading.Thread(target=listen,args=(8,))#listen(4)
t1.start()#start()->run()

t2=threading.Thread(target=eat,args=(4,))
t2.start()

t3=threading.Thread(target=drink,args=(3,))
t3.start()

t4=threading.Thread(target=listen,args=(7,))#listen(4)
t4.start()#start()->run()

#listen()
#eat()
#drink()

#Parent Thread -> Main Thread, Child Threads -> t1, t2, t3

#t1.join()
t3.join()
t2.join()


print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())
print(time.perf_counter())
print("End of Main Thread")


