import socket
def Main():
    host = '127.0.0.1'
    port = 1231
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #AF_INET - configures an IPV4 connection with Socket Streaming connection orienting TCP transmission
    #Steps are :
    #          1: configure your socket
    #          2: Connect your socket
    #          3: Send your data
    #          4: Close your connection
    s.connect((host,port))
    message = "This is Sarthak here!"
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('data received from the server: ',str(data.decode('ascii')))
        break
    s.close()
if __name__ == '__main__':
    Main()
