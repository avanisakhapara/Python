import threading
import time

# def eat():
#     #time.sleep(5)
#     for i in range(7):
#         time.sleep(5) # 5 secs
#         print("Finished eating fooditem",i+1)

# def pack():
#     for i in range(4):
#         time.sleep(3) # 3 secs
#         print("Finished packing item no",i+1)

# def news():
#     for i in range(3):
#         time.sleep(6) # 6 secs
#         print("Finished listening to news headlines",i+1)

# method 2 - inheriting Thread class -> threading.Thread

class eatThread(threading.Thread):
    
    def __init__(self,num_fooditems):
       #threading.Thread.__init__(self)
       super().__init__()
       self.num_fooditems = num_fooditems
       

    def eat(self):
    #time.sleep(5)
        for i in range(self.num_fooditems):
            time.sleep(3) # 5 secs
            print("Finished eating fooditem",i+1) 

    def run(self):
       self.eat()
        
t1 = eatThread(3)#calling constructor
t1.start()#start() ->run()

t1.join()

print(threading.current_thread())
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
print("End of Main Thread")



