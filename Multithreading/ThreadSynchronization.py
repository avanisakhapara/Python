import threading                         
import time

# def occupy(person,lock):    

#     lock.acquire() # current thread is acquiring the key to enter critical section
#     print(f"\n{person} occupied meeting room")
#     time.sleep(0.5)
#     print(f"\n{person} vacated meeting room")
#     lock.release() # current thread releases the key
   

# def occupy(person,lock):
#     lock.acquire(blocking=True, timeout=-1)
#     print(f"\n{person} occupied meeting room")
#     time.sleep(5)
#     print(f"\n{person} vacated meeting room")
#     lock.release()

# def occupy(person,lock):
#     while True:
#         if lock.acquire(timeout=0.1) == True:
#             break
#         else:
#             print(f'\n Lock is not available for {person}')

#     print(f"\n{person} occupied meeting room")
#     time.sleep(0.5)
#     print(f"\n{person} vacated meeting room")

#     lock.release()
    
def occupy(person,lock):
    while True:
        if lock.acquire(blocking=False) == True:
            break
        else:
            print(f'\n Lock is not available for {person}')

    print(f"\n{person} occupied meeting room")
    time.sleep(0.1)
    print(f"\n{person} vacated meeting room")

    lock.release()


lock = threading.Lock()
t1=threading.Thread(target=occupy,args=('John',lock))#occupy('John',lock)
t2=threading.Thread(target=occupy,args=('Peter',lock))

t1.start()
t2.start()

t1.join()
t2.join()


