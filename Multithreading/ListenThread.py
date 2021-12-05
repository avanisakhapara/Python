import threading
import time

# def listen(n1): #4
#     for i in range(n1):#i-> 0 to 3
#         time.sleep(4)
#         print(f"Finished listening to {i+1} session")

#method2 - inherit thread class

class ListenThread(threading.Thread): #start()
    def __init__(self,no_of_sessions,student_name):
       threading.Thread.__init__(self) 
       self.no_of_sessions = no_of_sessions
       self.student_name = student_name
       #super().__init__()

    # def listen(self):
    #     for i in range(self.no_of_sessions):#i-> 0 to 5
    #         time.sleep(4)
    #         print(f"Finished listening to {i+1} session by {self.student_name}")

    def run(self):
        for i in range(self.no_of_sessions):#i-> 0 to 5
            time.sleep(4)
            print(f"Finished listening to {i+1} session by {self.student_name}")
        #self.listen()
    

    # def start(self):
    #     #instructions to start the thread execution

t1 = ListenThread(8,"Peter")
t1.start()#start()->run()

#t1.join()

t2 = ListenThread(5,"Sam")
t2.start()


print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())
print(time.perf_counter())
print("End of Main Thread")


