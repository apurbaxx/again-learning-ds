##when to use multithreading
#I/O=bound tasks: Tasks that spend more time waiting for I/O operation(ex-file operation,network requests)
#When you want to improve throughput of your application by performing multiple operation concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(i)

def print_letters():
    for letter in 'abcdef':
        time.sleep(2)
        print(letter)


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t = time.time()
print(t)
#start the thread
t1.start()
t2.start()

t1.join()
t2.join()
ti = time.time()-t
print(ti)
