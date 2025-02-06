#github https://github.com/amir-kali-linux/
import socket
import time
print('------------(>ip-adress<)------------')
print('https://github.com/amir-kali-linux/')
time.sleep(4)
host=input('Enter web link:')
ipaddress=socket.gethostbyname(host)
print('web link :',host,'ip adress',ipaddress,)