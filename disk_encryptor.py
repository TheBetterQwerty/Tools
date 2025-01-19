#!/usr/bin/env python3

import base64
import os
import argparse
import hashlib
import random 
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(key: bytes, text: str) -> str:
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key,AES.MODE_CBC , iv)
    padded_text = pad(text, AES.block_size)
    encryption = base64.b64encode(cipher.encrypt(padded_text))
    return iv + encryption

def decrypt(key: bytes, encmsg: str) -> str:
    try:
        iv = encmsg[:AES.block_size]
        encmsg = encmsg[AES.block_size:]
        cipher = AES.new(key , AES.MODE_CBC , iv)
        decrypted = cipher.decrypt(base64.b64decode(encmsg))
        decrypted_text = unpad(decrypted, AES.block_size)
        return decrypted_text
    except :
        return 

def traverse(drive: str) -> list:
    req_files = []
    for root,_,files in os.walk(drive):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            req_files.append(file_path)
    return req_files

def encryptor(file: str, key: bytes) -> bool:
    try:
        with open(file , "rb") as f:
            file_contents = f.read()
    
        time = random.randint(1,9)

        for i in range(time):
            file_contents = encrypt(key , file_contents)

        with open(file , "wb") as f:
            f.write(file_contents + str(time).encode())
    except Exception as err:
        print(f"[!] Error {err}")
        return False
    else:
        return True

def decryptor(file , key) -> bool:
    try:
        with open(file , "rb") as f:
            file_contents = f.read()

        time = int(chr(file_contents[-1]))
        file_contents = file_contents[:-1]
        for i in range(time):
            file_contents = decrypt(key, file_contents)
            if not file_contents:
                print(f"[!] Decryption failed for {file}")
                return False
            
        with open(file , "wb") as f:
            f.write(file_contents)
    except Exception as err:
        print(f"[!] Error: {err}")
        return False
    else:
        return True

def main() -> None:
    parser = argparse.ArgumentParser(description=" *** Script To Encrypt Or Decrypt a Drive ***")
    parser.add_argument("-e", "--encrypt", type=str , help="Encrypts the drive")
    parser.add_argument("-d", "--decrypt" , type=str ,help="Decrypts the drive")
    args = parser.parse_args()
    
    if (args.encrypt and args.decrypt) or (not args.encrypt and not args.decrypt):
        print("[!] Please Specify a valid Operation! Press -h for help")
        return

    password: str = getpass("[?] Enter a password: ")
    _passwrd: str = getpass("[?] Enter password again: ")

    if not password == _passwrd:
        print("[!] Passwords don't match. Try again...")
        return

    key = hashlib.sha256(password.encode()).digest()
    if not os.path.exists(args.encrypt or args.decrypt):
        print("[!] Path Doesnt Exists")
        return

    files_found: list = traverse(args.encrypt or args.decrypt)
    if args.encrypt:
        for file in files_found:
            if encryptor(file , key):
                print(f"[#] Encrypted -> {file}")
    if args.decrypt:
        for file in files_found:
            if decryptor(file, key):
                print(f"[$] Decrypted -> {file}")

if __name__ == "__main__":
    main()
