import sys,os
import socket

def conect(ip,port):
    meusocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    res = meusocket.connect_ex((ip,port))
    print("Interagindo Com o Serviço")
    banner = meusocket.recv(1024)
    print(banner.decode())
    
    
    meusocket.send("USER anonymous\r\n".encode())
    banner = meusocket.recv(1024)
    print(banner.decode())
    
    meusocket.send("PASS anonymous\r\n".encode())
    banner = meusocket.recv(1024)
    print(banner.decode())

    #os.system(f"ping -c 1 {sys.argv[1]}")


def portscan(ip):
    for porta in range(1,65535):
        meusocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        if meusocket.connect_ex((ip,porta)) == 0:
            print(f"Porta {porta} [ABERTA]")
            meusocket.close()

def web():
    import requests
    from urllib.request import urlopen

    site = requests.get("http://google.com.br/")

    status = site.status_code

    if (status == 200):
        print('Existe')

    
    

    sitee = urlopen("http://google.com.br")
    server = sitee.info()


    #print(server['Server']) # 
    #print(sitee.read())
    #print(sitee.getcode()) #geturl()
    print(server)




ip = socket.gethostbyname(sys.argv[1])
#conect(ip,int(sys.argv[2]))
#portscan(ip)
#web()

