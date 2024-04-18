import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts";redirectredirect = "127.0.0.1"
web_list = []
n=int(input("Enter the  websites you want to block : "))
for i in range (n) :
    c=str(input("Enter website name : "))
    web_list.append(c)  

start = int(input("Enter the starting of your working hours : "))
end = int(input("Enter the ending of your working hours : "))
while True:
  
     if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23) :
         print("Working hours...")
         with open(hosts_path, 'r+') as file:
             content = file.read()
             for website in web_list:
                 if website in content:
                     pass
                 else:
                     file.write(redirect + " " + website + "\n")
     else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
file.truncate()
  
print("Fun hours...")
time.sleep(5)
