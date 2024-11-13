#!/bin/bash/env python3

import socket
import threading 
import os
import random 



def port_scanner():
    ports = {
    20: "FTP (File Transfer Protocol) - Data transfer",
    21: "FTP (File Transfer Protocol) - Command/control",
    22: "SSH (Secure Shell) - Secure login and file transfer",
    23: "Telnet - Unencrypted text communications",
    25: "SMTP (Simple Mail Transfer Protocol) - Email routing",
    53: "DNS (Domain Name System) - Translates domain names to IP addresses",
    67: "DHCP (Dynamic Host Configuration Protocol) - Assigns IP addresses (server)",
    68: "DHCP (Dynamic Host Configuration Protocol) - Assigns IP addresses (client)",
    80: "HTTP (Hypertext Transfer Protocol) - Web browsing",
    110: "POP3 (Post Office Protocol) - Retrieves emails",
    123: "NTP (Network Time Protocol) - Synchronizes clocks",
    143: "IMAP (Internet Message Access Protocol) - Retrieves emails",
    161: "SNMP (Simple Network Management Protocol) - Network management",
    194: "IRC (Internet Relay Chat) - Chat service",
    443: "HTTPS (HTTP Secure) - Secure web browsing",
    445: "SMB (Server Message Block) - File sharing on Windows networks",
    465: "SMTPS (SMTP Secure) - Secure email routing",
    993: "IMAPS (IMAP Secure) - Secure email retrieval",
    995: "POP3S (POP3 Secure) - Secure email retrieval",
    1433: "MSSQL - Microsoft SQL Server communication",
    1723: "PPTP (Point-to-Point Tunneling Protocol) - VPN communication",
    3306: "MySQL - Database communication",
    3389: "RDP (Remote Desktop Protocol) - Remote desktop access",
    5432: "PostgreSQL - Database communication",
    5900: "VNC (Virtual Network Computing) - Remote desktop control",
    8080: "HTTP (alternative) - Web browsing"
    }

    def is_port_open(host, port)->None:
        s = socket.socket()
        s.settimeout(10)
        try:
            s.connect((host, port))
        except :
            pass
        else:
            print(f"[*] Port {port} is opened and its used is {ports.get(port,'unknown')}")

    def main()->None:
        threads = []
        target_host = input(f"Enter the target host (e.g., example.com) >> ")
        for i in range(1, 65535):
            t = threading.Thread(target=is_port_open , args=(target_host,i))
            t.start()
            threads.append(t)
        
        for thread in threads:
            thread.join()

    main()




def PDFcracker():
    try:
        import PyPDF2 #type:ignore
    except ModuleNotFoundError :
        print("PyPDF2 module was not found \nPlease install it then try again")
        exit(1)

    def read_pdf(pdf) -> bool:
        with open (pdf , "rb") as file:
                reader = PyPDF2.PdfReader(file)
                password = bruteforce(5)
                if reader.is_encrypted:
                        try:
                                reader.decrypt(password)
                                print("Password found -> " , password)
                                return True
                        except Exception as e:
                                return False
                else:
                        print("File is not encrypted !!")
                        return True


    def bruteforce(length) -> str:
            string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#!@$%^&*"
            guesspass = ""
            for i in range(length):
                    index = random.randint(0,69)
                    guesspass += string[index]
            return guesspass

    def main() -> None:
            Threads = []
            file_path = input("Enter the path of file -> ")
            if (os.path.exists(file_path)== False):
                    print("File Dosnt Exists !!")
                    exit(1)
            
            for i in range(100):
                    T = threading.Thread(read_pdf, file_path)
                    Threads.append(T)
            
            for i in range(100):
                    Threads[i].start()
            for i in range(100):
                    Threads[i].join()
    main()

req = 0

def NGL_spam():
    try:
        import requests 
    except ModuleNotFoundError:
        print("Requests Module was not found\nPlease install it then try again ")
        exit(1)

    url = "https://ngl.link/api/submit"

    username = input("Enter the Username of the target >> ")

    txt = input("Enter Text >>> ")

    data = {
        'username': username,
        'question': txt, 
        'deviceId': '5adh65ye-b542-48g5-b76a-33765y242e59',
        'gameSlug': '' ,
        'referrer': '',
    }

    def make_requests():
        global req
        while True:
            try:
                response = requests.post(url , data=data).text
                req += 1
                print(f"Message send to {username} : {req}")
            except KeyboardInterrupt:
                break

    def main():
        threads = []
        for i in range(50):
            t = threading.Thread(target=make_requests)
            t.start()
            threads.append(t)
        
        for thread in threads:
            thread.join()

    main()


if __name__ == "__main__":
    
    print("*"*10 , "@QWERTY@ Projects", "*"*10)
    print("1) Press 1 for Portscanning ")
    print("2) Press 2 for cracking a PDF file that is encrypted ")
    print("3) Press 3 to spam someones NGL ")
    print("99) Press 99 to EXIT")
    try:    
        choice = int(input("[*] Enter Your Choice >> "))
        if choice == 1 :
            port_scanner()
        if choice == 2:
            PDFcracker()
        if choice == 3 :
            NGL_spam()
        if choice == 99 :
            exit(0)
    except:
        exit(1)

