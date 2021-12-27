import socket

ClientSocket = socket.socket()
host = '192.168.56.102'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

response = ClientSocket.recv(1024).decode('utf-8')
print(response)

while True:
    print("\nSelect operation.\n1.Logarithmic \n2.Square Root\n3.Exponential\nQ to quit \n")
    choice = input('Select 1/2/3: ')
    ClientSocket.send(str.encode(choice))
    
    #Logarithmic and square root function
    if choice == '1' or choice == '2' :
        num1 = input("Enter a number: ")
        ClientSocket.send(str.encode(num1))
     
    #Exponential function
    elif choice == '3':
        num1 = input("Enter a number: ")
        num2 = input("Enter exponent value: ")
        ClientSocket.sendall(str.encode("\n".join([str(num1), str(num2)])))
    
    #Terminate connection
    elif choice == 'Q' or choice == 'q':
        print("Closing client connection, goodbye")
        break
        
    result = ClientSocket.recv(1024).decode('utf-8')
    print(result) 
  
ClientSocket.close()
