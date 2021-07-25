import time
from datetime import datetime as dt

hostsPath = r"/etc/hosts"
# hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ["www.youtube.com", "youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18) :
        print("Not allowed")
        with open(hostsPath,'r+') as file:
         content=file.read()
         for site in websites:
                if site in content:
                  pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        with open(hostsPath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
                file.truncate()
            print("Allowed")
        time.sleep(3)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
