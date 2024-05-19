import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(3)

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2,3,8]
    
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  
     
    print("done in : ",time.time()-t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count()) 
    
########################
# importing the multiprocessing module 
import multiprocessing 
import os 

def worker1(): 
	# printing process id 
	print("ID of process running worker1: {}".format(os.getpid())) 

def worker2(): 
	# printing process id 
	print("ID of process running worker2: {}".format(os.getpid())) 

if __name__ == "__main__": 
	# printing main program process id 
	print("ID of main process: {}".format(os.getpid())) 

	# creating processes 
	p1 = multiprocessing.Process(target=worker1) 
	p2 = multiprocessing.Process(target=worker2) 

	# starting processes 
	p1.start() 
	p2.start() 

	# process IDs 
	print("ID of process p1: {}".format(p1.pid)) 
	print("ID of process p2: {}".format(p2.pid)) 

	# wait until processes are finished 
	p1.join() 
	p2.join() 

	# both processes finished 
	print("Both processes finished execution!") 

	# check if processes are alive 
	print("Process p1 is alive: {}".format(p1.is_alive())) 
	print("Process p2 is alive: {}".format(p2.is_alive())) 

################################

#This example demonstrate shared data space by different processes(problem)

import multiprocessing 

# empty list with global scope 
result = [] 

def square_list(mylist): 
	""" 
	function to square a given list 
	"""
	global result 
	# append squares of mylist to global list result 
	for num in mylist: 
		result.append(num * num) 
	# print global list result 
	print("Result(in process p1): {}".format(result)) 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
	# starting process 
	p1.start() 
	# wait until process is finished 
	p1.join() 

	# print global result list 
	print("Result(in main program): {}".format(result)) 

	"""
	In above example, we try to print contents of global list result at two places:
	-In square_list function. Since, this function is called by process p1, result list is changed in memory space of process p1 only.
	-After the completion of process p1 in main program. Since main program is run by a different process, its memory space still contains the empty result list.
	"""

##############################

#This example demonstrate shared data space by different processes (solution)

import multiprocessing 

def square_list(mylist, result, square_sum): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to result array 
	for idx, num in enumerate(mylist): 
		result[idx] = num * num 

	# square_sum value 
	square_sum.value = sum(result) 

	# print result Array 
	print("Result(in process p1): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in process p1): {}".format(square_sum.value)) 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating Array of int data type with space for 4 integers 
	result = multiprocessing.Array('i', 4) 

	# creating Value of int data type 
	square_sum = multiprocessing.Value('i') 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum)) 

	# starting process 
	p1.start() 

	# wait until the process is finished 
	p1.join() 

	# print result array 
	print("Result(in main program): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in main program): {}".format(square_sum.value)) 


"""
	Shared memory : multiprocessing module provides Array and Value objects to share data between processes.
	Array: a ctypes array allocated from shared memory.
	Value: a ctypes object allocated from shared memory.
"""
##################################33
#This example demonstrate communications between processes
"""
Effective use of multiple processes usually requires some communication between 
them, so that work can be divided and results can be aggregated.
multiprocessing supports two types of communication channel between processes:
-Queue
-Pipe
"""
# Queue Example

import multiprocessing 

def square_list(mylist, q): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to queue 
	for num in mylist: 
		q.put(num * num) 

def print_queue(q): 
	""" 
	function to print queue elements 
	"""
	print("Queue elements:") 
	while not q.empty(): 
		print(q.get()) 
	print("Queue is now empty!") 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating multiprocessing Queue 
	q = multiprocessing.Queue() 

	# creating new processes 
	p1 = multiprocessing.Process(target=square_list, args=(mylist, q)) 
	p2 = multiprocessing.Process(target=print_queue, args=(q,)) 

	# running process p1 to square list 
	p1.start() 
	p1.join() 

	# running process p2 to get queue elements 
	p2.start() 
	p2.join() 
########################3
#This example demonstrate communications between processes
"""
Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.
multiprocessing supports two types of communication channel between processes:
-Queue
-Pipe
"""
"""
Pipes : A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required. 
multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. 
The two connection objects returned by Pipe()represent the two ends of the pipe. Each connection object has send() 
and recv() methods (among others).
"""
# Pipe Example

import multiprocessing 

def sender(conn, msgs): 
	""" 
	function to send messages to other end of pipe 
	"""
	for msg in msgs: 
		conn.send(msg) 
		print("Sent the message: {}".format(msg)) 
	conn.close() 

def receiver(conn): 
	""" 
	function to print the messages received from other 
	end of pipe 
	"""
	while 1: 
		msg = conn.recv() 
		if msg == "END": 
			break
		print("Received the message: {}".format(msg)) 

if __name__ == "__main__": 
	# messages to be sent 
	msgs = ["hello", "hey", "hru?", "END"] 

	# creating a pipe 
	parent_conn, child_conn = multiprocessing.Pipe() 

	# creating new processes 
	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

	# running processes 
	p1.start() 
	p2.start() 

	# wait until processes finish 
	p1.join() 
	p2.join() 

    