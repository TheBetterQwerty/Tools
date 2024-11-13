#!/usr/bin/env python3

import argparse
import requests
import threading

def response(subdomains, output=""):
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            if output != "":
                with open(output, "a") as file:
                    file.write(subdomain + "\n")
            if response.status_code != 200:
                print(f"{subdomain} [\033[31m{response.status_code}\033[0m]")
            else:
                print(f"{subdomain} [\033[32m{response.status_code}\033[0m]")
        except Exception as e:
            pass

def subdomains(domain, files):
    try:
        with open(files) as file:
            _subdomains = file.read().split("\n")
    except FileNotFoundError:
        print("file not found")
        exit()

    _subdomains = [f"https://{subdomain}.{domain}" for subdomain in _subdomains if not subdomain.isdigit()]
    return _subdomains

def domain(domain, file, t):
    _subdomains = subdomains(domain, file)
    threads = []
    for i in range(0, len(_subdomains), t):
        thread = threading.Thread(target=response, args=(_subdomains[i:i+t],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=" *** Script to find subdomains *** ")
    parser.add_argument("-d", "--domain", required=True, type=str, help="domain to scan")
    parser.add_argument("-w", "--wordlist", required=True, type=str, help="path to wordlist")
    parser.add_argument("-t", "--threads", default=20, required=False, type=int, help="number of threads to use (default: 20)")
    parser.add_argument("-o", "--output", default="", required=False, type=str, help="working subdomains output to a file")
    args = parser.parse_args()

    domain(args.domain, args.wordlist, args.threads)
