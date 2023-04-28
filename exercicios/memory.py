from subprocess import check_output
from time import sleep
import sys

while True:
    memory_information = [
        information
        for information in check_output("free")
        .decode("UTF-8")
        .split("\n")[1]
        .split(" ")
        if information != ""
    ]

    total_memory = int(memory_information[1]) / 1000
    used_memory = int(memory_information[2]) / 1000

    print(
        f"Memória total: {total_memory:.0f}MB\n"
        f"Memória utilizada: {used_memory:.0f}MB",
    )

    sys.stdout.write("\033[2F")

    sleep(1)
