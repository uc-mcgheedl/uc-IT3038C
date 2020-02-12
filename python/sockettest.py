import socket, sys


hosts = ["www.uc.edu", "www.google.com", "www.reddit.com"]
print("working from host: " + socket.getfqdn())
for h in hosts:
    print(h + ": " + socket.gethostbyname(h))