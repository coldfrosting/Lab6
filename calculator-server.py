import socket
import sys
import time
import errno
import math
from multiprocessing import Process


def process_start(s_sock):
    s_sock.send(str.encode("Welcome to the Online Calculator!"))
    while True:
        data = s_sock.recv(2048).decode('utf-8')
        
        #Base 10 Log()
        if data == '1':
            num1 = int(s_sock.recv(2048).decode('utf-8'))
            print("Log(%d)" % num1)
            result = math.log(num1,10)
            
        #Square root function
        elif data == '2':
            num1 = int(s_sock.recv(2048).decode('utf-8'))
            print("sqrt(%d)" % num1)
            result = math.sqrt(num1)
           
        #Exponential function
        elif data == '3':
            num1, num2 = [int(i) for i in s_sock.recv(2048).decode('utf-8').split('\n')]
            print(str(num1)+"^"+str(num2))
            result = pow(num1,num2)
            
        #Terminate client connection
        elif data == "Q" or data == "q":
            print("Client has terminate function")
            break  
            
        print(result)   
        output = "The result is %s" % str(result)
        s_sock.send(str.encode(output))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()
             
            except socket.error:

                print('got a socket error')

    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	   s.close()
