#!/usr/bin/python3
import scapy.all as scapy
from scapy.utils import wrpcap
import argparse
from datetime import datetime
import os

def sniff(interface ,f):
    packets = scapy.sniff(iface=interface , filter=f , prn=lambda x:f"[*] {x.summary()}")
    return packets

if __name__ == '__main__' :
    if os.getuid() != 0:
        print(f'Use the program in super user mode ')
        exit()
    parser = argparse.ArgumentParser(description="Script to sniff packets from the selected interface.")
    parser.add_argument("-i" , "--interface" , type=str , required=True , help="Your Interface")
    parser.add_argument("-f" , "--filter" , type=str , default=" " , required=False , help="Filter (optional)")
	
    args = parser.parse_args()
    interface = args.interface
    filters = args.filter
    time = datetime.now()
    print(f"Starting sniffer at {time}")
    print(f"InterFace ->> {interface}\n")

    packets = sniff(interface,filters)

    write = input(r"Do you want to write this into a pcap file? (N\Y) ")

    if (write in ['Y' , 'y']):
        path = input("Enter the Path where to store it ->> ")
        try:
            wrpcap(rf"{path}", packets)
            print(f"Saved Pcap File to {path}")
        except Exception as e:
            print(f"Error {e}")
