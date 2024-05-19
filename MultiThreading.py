
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:14:46 2024

@author: Ahmed Elsheikh
"""
#This is sequential program

import time

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)


print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")

############################33
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:14:46 2024

@author: Ahmed Elsheikh
"""
#This is multithreaded program uses I/O bound tasks to speed up the program
#Study the effect of join function

import time
import threading

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
###########################3
"""
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 
The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 
"""
# Simple example

import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")

###############################33
"""
A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks. 
The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool. 
"""

#Another Example

import time
import concurrent.futures

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(1)
 

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(1)


arr = [2,3,8]

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(calc_square , arr) 
pool.submit(calc_cube , arr)

pool.shutdown(wait=True)

print("Main thread continuing to run")
############################


#Race Condition Problem

import threading 

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(): 
	""" 
	task for thread 
	calls increment function 1000 times. 
	"""
	for _ in range(100000): 
		increment() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = threading.Thread(target=thread_task) 
	t2 = threading.Thread(target=thread_task) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 

#########################33
#Race Condition Problem Solution using Lock Class

import threading 

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(lock): 
	""" 
	task for thread 
	calls increment function 100000 times. 
	"""
	for _ in range(100000): 
		lock.acquire() 
		increment() 
		lock.release() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating a lock 
	lock = threading.Lock() 

	# creating threads 
	t1 = threading.Thread(target=thread_task, args=(lock,)) 
	t2 = threading.Thread(target=thread_task, args=(lock,)) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 

##########################3

#This example demostrates the use of events to coordinate threads: one thread signals an event while other threads wait for it.

from threading import Thread, Event
from time import sleep

def task(event: Event, id: int) -> None:
    print(f'\nThread {id} started. Waiting for the signal....')
    event.wait() #Tell thread to wait until thread is set
    print(f'\nReceived signal. The thread {id} was completed.')

def main() -> None:
    event = Event() #reate a new Event object:

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(3) 
    event.set() #Set the event



if __name__ == '__main__':
    main()
