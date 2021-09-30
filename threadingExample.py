import threading
from queue import Queue
import time

# When we have a shared variable, we need to be able to lock it so that only
# one thread at a time can use it
print_lock = threading.Lock()

def exampleJob(worker):
  time.sleep(0.5)

  with print_lock:
    print(threading.current_thread().name, worker)

def threader():
  while True:
    worker = q.get()
    exampleJob(worker)
    q.task_done()

q = Queue()

# Make 10 threads
for x in range(10):
  thread = threading.Thread(target=threader)
  thread.daemon = True
  thread.start()

start = time.time()

# Make 20 jobs
for worker in range(20):
  q.put(worker)

q.join()

print('Entire job took: ', time.time()-start)