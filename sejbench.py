import os
import random
import time
from decimal import Decimal, getcontext
from urllib.request import urlretrieve

print("Running SejBench...")

getcontext().prec = 50  # Pin precision
cpu_start = time.time()
a = Decimal()
for i in range(250):
    a += Decimal.sqrt(Decimal(i**13337))
cpu_time = time.time() - cpu_start

print(f"CPU Test: {round(cpu_time, 2)}s")

gb = 1
size = gb * (1024**3)
mem_start = time.time()
# Create
arr1 = bytearray(size)
for i in range(0, size, 4096):
    arr1[i] = 1
# Copy
arr2 = bytearray(size)
arr2[:] = arr1
# Random Access
rng = random.Random(0)
total = 0
for _ in range(4_000_000):
    total += arr1[rng.randrange(size)]
del arr1, arr2
mem_time = time.time() - mem_start

print(f"Memory Test: {round(mem_time, 2)}s")

file_start = time.time()
file_name = "sejbench-file.txt"
payload = "123456789" * 100_000
for i in range(1500):
    with open(file_name, "w") as f:
        f.write(payload)
        f.flush()
        os.fsync(f.fileno())
    os.remove(file_name)
file_time = time.time() - file_start

print(f"File Test: {round(file_time, 2)}s")

download_start = time.time()
download_name = "sejbench-download"
urlretrieve("https://github.com/mikkelmk/sejbench-files/raw/main/100MB", download_name)
os.remove(download_name)
download_time = time.time() - download_start

print(f"Download Test: {round(download_time, 2)}s")
