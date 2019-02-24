import socket
#importing multithreading libraries
from _thread import *
import threading

#create lock object
print_lock = threading.Lock()

#thread function
def threaded(c):
    while True:

        #Receive data from the client
        data = c.recv(1024) #receiving 1024 bytes at a time
        if not data:
            print("Bye")
            print_lock.release()
            break
        #We want to reverse the data sent by client. This is the processing portion of the server
        data = data[::-1]

        # send the reversed data back to the client
        c.send(data)
    c.close()
    #closing the connection with the client

def Main():
    host = ""
    port = 1231 #Can be any 16 bit number in range 0 to 65535
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    print("socket binded to the post",port)
    # put the socket into the listening mode 
    s.listen(10)
    print("Socket is listening")
    while True:
        c,address = s.accept()
        print_lock.acquire()
        print("Connected to the client ",address[0],":",address[1])

        #Start a new thread and return its identifier
        start_new_thread(threaded,(c,))
    s.close()
if __name__ == '__main__':
    Main()