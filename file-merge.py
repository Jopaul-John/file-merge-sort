import os
import random
import sys
import threading
import concurrent.futures

NUM_OF_FILES = 1000


def create_file():
    for i in range(NUM_OF_FILES):
        with open(f"file{i}.txt", "w") as fp:
            fp.write(f"{str(random.random())} on file {i}")


def delete_file():
    for i in range(NUM_OF_FILES):
        os.remove(f"file{i}.txt")


def merge_file(file_names):
    while len(file_names) >= 3:
        for i in range(int(len(file_names))):
            index = i * 2
            try:
                with open(f"file{i}.txt", "r") as fp2:
                    data2 = fp2.read()
                with open(f"file{i+1}.txt", "r") as fp1:
                    data1 = fp1.read()
                with open(f"file{i+1}.txt", "w") as fp1:
                    fp1.write(data2)
                    fp1.write("\n")
                    fp1.write(data1)
                os.remove(f"file{i}.txt")
                file_names.remove(f"file{i}.txt")
            except FileNotFoundError:
                print("")

def join():
    file_names = [f"file{i}.txt" for i in range(NUM_OF_FILES)]
    if NUM_OF_FILES % 2 == 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(merge_file(file_names))
    last_file = NUM_OF_FILES -1
    with open(f"file{last_file}.txt", 'r') as fp:
        lines = fp.readlines()
    with open(f"file{last_file}.txt", 'w') as fp:
        lines.sort()
        fp.writelines(lines)


def main():
    if sys.argv[1] == "createfile":
        create_file()
    elif sys.argv[1] == "deletefile":
        delete_file()
    elif sys.argv[1] == "joinfile":
        join()


if __name__ == "__main__":
    main()
