# trainer.py
from collections import Counter
import os
import socket
import sys
import time
import ray

num_cpus = int(sys.argv[1])

ray.init(address=os.environ["thishostNport"])

print("Nodes in the Ray cluster:")
print(ray.nodes()) # This should print all N nodes we are trying to access


@ray.remote
def f():
    time.sleep(1)
    return socket.gethostbyname(socket.gethostname()) + "--" + str(socket.gethostname())


# The following takes one second (assuming that
# ray was able to access all of the allocated nodes).
for i in range(60):
    start = time.time()
    ip_addresses = ray.get([f.remote() for _ in range(num_cpus)])
    print("GOT IPs", ip_addresses)
    print(Counter(ip_addresses))
    end = time.time()
    print(end - start)