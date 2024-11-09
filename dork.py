base_url = "https://www.google.com/search?q="
  2 dir_list = {}
  3
  4 def banner():
  5     ban = '''*** Google Dorking Tool ***
  6                 - qwerty'''
  7     print(ban)
  8
  9 def url_dorking():
 10     url = input("Enter the url -> ")
 11     if not url :
 12         print("No url given exitting")
 13         exit()
 14     dir_list["Directory Listing"] = f"{base_url}site:{url}+intitle:index.of"
 15     dir_list["Config Files"] = f"{base_url}site:{url}+ext:xml%20|%20ext:conf%20|%20ext:cnf%20|%20ext:reg%20|%20ext:i    nf%20|%20ext:rdp%20|%20ext:cfg%20|%20ext:txt%20|%20ext:ora%20|%20ext:ini"
 16     dir_list["Log Files"] = f"{base_url}site:{url}+ext:log"
 17     dir_list["BackUp Files"] = f"{base_url}site:{url}+ext:bkf%20|%20ext:bkp%20|%20ext:old%20|%20ext:backup"
 18     dir_list["HTA access"] = f'{base_url}site:{url}+inurl:"/phpinfo.php"%20|%20inurl:".htaccess"'
 19     dir_list["Robots.txt"] = f"{base_url}site:{url}/robots.txt"
 20
 21 if __name__ == "__main__":
 22     banner()
 23     ch = input("Enter 1 for url dorking or 2 for person dorking : ")
 24     if ch == "1":
 25         url_dorking()
 26         print("*** Links ***")
 27         for i , j in dir_list.items():
 28             print(f"{i} -> {j}")
