import os
import time
from decimal import Decimal
from urllib.request import urlretrieve

print("Running SejBench...")

cpu_start = time.time()
a = Decimal()
for i in range(250):
    a += Decimal.sqrt(Decimal(i**13337))
cpu_time = time.time() - cpu_start

print(f"CPU Test: {round(cpu_time, 2)}s")

file_start = time.time()
file_name = "sejbench-file.txt"
for i in range(1500):
    with open(file_name, "w") as f:
        f.write("123456789" * 1000 * i)
    os.remove(file_name)
file_time = time.time() - file_start

print(f"File Test: {round(file_time, 2)}s")

download_start = time.time()
download_name = "sejbench-download"
urlretrieve("https://github.com/mikkelmk/sejbench-files/raw/main/100MB", download_name)
os.remove(download_name)
download_time = time.time() - download_start

print(f"Download Test: {round(download_time, 2)}s")
