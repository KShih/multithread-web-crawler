import heapq
import logging
import threading
import random
import time
import concurrent.futures

heap = [1,2,3,4,5,6,7,8,9,10]
heapq.heapify(heap)
visited = set()
for i in range(1, 11):
  visited.add(i)
visited_lock = threading.Lock()

def parse(name, url_num):
  logging.info("This url score is: %d found in thread: %d", url_num, name)

  news = [random.randint(1, 100) for _ in range(10)]
  time.sleep(2)

  for new in news:
    visited_lock.acquire()
    if new not in visited:
      # logging.info("Add new: %d", new)
      heapq.heappush(heap, new)
      visited.add(new)
    visited_lock.release()
  logging.info("Thread %s: finishing", name)

def read():
  logging.info("Length of heap %d", (len(heap)))
  logging.info("Length of visited %d", (len(visited)))
  time.sleep(2)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        while True:
          read()
          for idx in range(3):
            if heap:
              elem = heapq.heappop(heap)
              executor.submit(parse, idx, elem)