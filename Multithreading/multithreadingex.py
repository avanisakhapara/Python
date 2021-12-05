import threading
import time

def eat(n1):
    #time.sleep(5)
    for i in range(n1):
        time.sleep(5) # 5 secs
        print("Finished eating fooditem",i+1)

def pack(n2):
    for i in range(n2):
        time.sleep(3) # 3 secs
        print("Finished packing item no",i+1)

def news(n3):
    for i in range(n3):
        time.sleep(6) # 6 secs
        print("Finished listening to news headlines",i+1)


# method 1 - using callable object

t1 = threading.Thread(target=eat,args=(7,)) # created Thread object -child
#t1.start() #start() -> run()

t2 = threading.Thread(target=pack,args=(4,)) # created Thread object -child
#t2.start()

t3 = threading.Thread(target=news,args=(3,)) # created Thread object -child
#t3.start()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# eat()
# pack()
# news()

# join () Parent thread waits for child thread to terminate. After that parent thread terminates
#t1.join()
#t2.join()
#t3.join()

print(threading.current_thread())
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
print("End of Main Thread")

#Parent thread got terminated first - main
# after that child threads got ternimated-Thread-2->Thread-1->Thread-3

