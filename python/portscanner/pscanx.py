import socket
from datetime import datetime

def is_port_open(host, port):
    s = socket.socket()
    #s.settimeout(0.2) 
    try:
        s.connect((host, port))
    except socket.error:
        return False
    else:
        return True

host = input("Enter the host: ")
t1 = datetime.now()

for port in range(0, 1024): # change the port scan range
    if is_port_open(host, port):
        print(f"[+] {host}:{port} is open  ")
    else:
        print(f"[!] {host}:{port} is closed", end="\r")

t2 = datetime.now()
total_time = t2 - t1

print(f"[>] Scanning complete in {total_time}")
