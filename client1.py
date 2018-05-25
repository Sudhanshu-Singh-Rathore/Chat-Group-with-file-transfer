import socket
import select
import sys

 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
 
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
 
    """ There are two possible input situations. Either the
    user wants to give  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        
        if socks == server:
            message = socks.recv(2048)
            
            y=0
            for letter in message:
                
                if(letter=="1" and y>12):
                    
                    print "do you want to recieve file"
                    k=input()
                    if(k==0):
                        break
                    if(k==1):
                    
                        s = socket.socket()             # Create a socket object
                        host = socket.gethostname()     # Get local machine name
                        port = 60000                    # Reserve a port for your service.

                        s.connect((host, port))
                        s.send("Hello server!")

                        with open('received_file', 'wb') as f:
                            print 'file opened'
                            while True:
                                print('receiving data...')
                                data = s.recv(1024)
                                print('data=%s', (data))
                                if not data:
                                    break
                                # write data to a file
                                f.write(data)

                        f.close()
                        print('Successfully get the file')
                        s.close()
                        print('connection closed')
                        break
                y+=1
            print message
        else:
            print "press 1 for sending any file"
            message = raw_input()
            if (message=='1'):
                
                server.send(message)
                port = 60000                    # Reserve a port for your service.
                s = socket.socket()             # Create a socket object
                host = socket.gethostname()     # Get local machine name
                s.bind((host, port))            # Bind to the port
                s.listen(5)                     # Now wait for client connection.

                print 'Server listening....'
                o=1
                while (o==1):
                    conn, addr = s.accept()     # Establish connection with client.
                    print 'Got connection from', addr
                    data = conn.recv(1024)
                    print('Server received', repr(data))

                    filename='mytext.txt'
                    f = open("/home/sudhanshu/Desktop/sample_video.mp4",'rb')
                    l = f.read(1024)
                    while (l):
                        conn.send(l)
                        print('Sent ',repr(l))
                        l = f.read(1024)
                    f.close()
                    o=0
                    print('Done sending')
                    conn.send('Thank you for connecting')
                    conn.close()
                    m='0'
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
            message="0"
server.close()
