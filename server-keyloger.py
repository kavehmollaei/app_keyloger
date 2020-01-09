from socket import *
def start():

    s=socket(AF_INET,SOCK_STREAM)
    s.bind(('127.0.0.1',1222))
    s.listen(5)
    client,addr = s.accept()
    while True:
        data = client.recv(1024)
        data = data.decode('utf-8')
        if data[0]=='m':

            data=data[1:]
            with open('mouse.txt','a+') as fp :
                fp.write(data)
                fp.close()
        else:
            if data[0]=='k':
                data=data[1:]
                with open('keyboard.txt','a+') as fp :
                    fp.write(data)
                    fp.close()
    client.close()
start()
