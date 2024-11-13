#!/usr/bin/python3

from scapy.all import *
import threading 
import sys
import logging 
import os

alive_host = []
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def ipaddresses(CIDRip):
	network_range = Net(CIDRip)
	valid_ips = [str(ip) for ip in network_range]
	return valid_ips

def hostalive(ip):
	packet = ARP(pdst=ip)
	arp_res = sr1(packet , timeout = 2 , verbose=False)
	if arp_res is not None :
		return True
	return False

def main(ips):
	global alive_host
	for ip in ips:
		if hostalive(ip):
			alive_host.append(ip)
		
if __name__ == "__main__":
    if os.getuid() != 0:
        print("Please use sudo to run the script")
        sys.exit()

    if len(sys.argv) < 2 :
        print("Usage: sudo python hostfind.py 192.168.0.1/24")
        sys.exit()

    CIDRip = sys.argv[1]
    valid_ips = ipaddresses(CIDRip)
    start , end = 0 , 17
    threads = []
    print(f"[*] Starting To send ARP packets...")
    while start < len(valid_ips):
        ips = valid_ips[start:end]
        t = threading.Thread(target=main , args=(ips,))
        t.start()
        threads.append(t)
        start += 17
        end += 17

    for thread in threads:
        thread.join()

    for host in alive_host:
        print(f"{host} is up")
