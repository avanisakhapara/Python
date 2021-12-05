import threading
import time



# def eat():
#     time.sleep(6)
#     print(f"Finished eating Breakfast")

# def pack():
#     time.sleep(3)
#     print("Finished packing bag")

# def news():
#     time.sleep(4)
#     print("Finished listening to news headlines")




# # method 1: using callable object
# t1 = threading.Thread(target=eat)
# t1.start()


# t2 = threading.Thread(target=pack)
# t2.start()

# t3=threading.Thread(target=news)
# t3.start()

# method2: Inheriting Thread class
class Eat(threading.Thread):

    def __init__(self,eat_time,pname):
        threading.Thread.__init__(self)
        self.eat_time = eat_time
        self.pname=pname
        pass

    def eat(self):
        time.sleep(self.eat_time)
        print(f"{self.pname} has Finished Eating")

    def run(self):
        # time.sleep(6)
        # print("Finished Eating")
        self.eat()

t1=Eat(6,'John')#John
t1.start()#->run()
t1.join()

t2=Eat(2,'Peter')#Peter
t2.start()




# eat()
# pack()
# news()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
print("End of Main Thread")
