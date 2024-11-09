base_url = "https://www.google.com/search?q="
dir_list = {}

def banner():
    ban = ''' *** Google Dorking Tool *** 
                        -qwerty'''
    print(ban)

def url_dorking():
    url = input("Enter the url -> ")
    if not url and ".com" not in url :
        print("Not a valid url given")
        exit()
    dir_list["Dir List"] = f"{base_url}site:{url}+intitle:index.of"
    dir_list["Config Files"] = f"{base_url}site:{url}+ext:xml%20|%20ext:conf%20|%20ext:cnf%20|%20ext:reg%20|%20ext:inf%20|%20ext:rdp%20|%20ext:cfg%20|%20ext:txt%20|%20ext:ora%20|%20ext:ini"
    dir_list["Log Files"] = f"{base_url}site:{url}+ext:log"
    dir_list["Backup Files"] = f"{base_url}site:{url}+ext:bkf%20|%20ext:bkp%20|%20ext:old%20|%20ext:backup"
    dir_list["HTA access"] = f'{base_url}site:{url}+inurl:"/phpinfo.php"%20|%20inurl:".htaccess"'
    dir_list["Robots.txt"] = f"{base_url}site:{url}/robots.txt"

if __name__ == "__main__":
    banner()
    ch = int(input(" Url Dorking or Person Dorking(1/0) -> "))
    if ch == 1:
        url_dorking()
        print("Links are : ")
        for i,j in dir_list.items():
            print(f"{i} : {j}")
    elif ch == 0:
        print("Comming soon")
    else:
        print("Not a valid choice")
