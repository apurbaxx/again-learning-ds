##Processes that run in parallel
###CPU bound tasks - Tasks that rely on heavy cpu usage
### Parallel execution - Multiple cores of the cpu

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i**2}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i**3}")

##create two process
if __name__=="__main__":
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(f"Finished in {finished_time} seconds")