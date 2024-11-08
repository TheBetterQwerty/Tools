import requests

base_url = "https://www.google.com/search?q="
a = "https://www.youtube.com/watch?v=yINbDd6Hn4c"

def banner():
	ban = '''*** Google Dorking Tool ***
	            - qwerty'''
	print(ban)

def url_dorking():
	url = input("Enter the url -> ")
	if not url :
		print("No url given exitting")
		exit()
	dir_list = []
	dir_list.append(f"{base_url}site:{url}+intitle:index.of")
	dir_list.append(f"{base_url}site:{url}+ext:(xml|conf|cnf|reg")

if __name__ == "__main__":
	banner()
	ch = input("Enter 1 for url dorking or 2 for person dorking : ")
	if ch == "1":
		url_dorking()
