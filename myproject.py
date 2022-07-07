from socket import * #to import socket module/libraries


serverPort = 9000
serverSocket = socket(AF_INET,SOCK_STREAM) #creating TCP socket server 
serverSocket.bind(("",serverPort)) #binding server socket to all network interfaces
serverSocket.listen(1) #wait for the client connection
print ("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept() #accept client connection #connectionSocket is the client socket and addr is the client address 
    ip = addr[0]
    port = addr[1]
    
    sentence = connectionSocket.recv(1024).decode() #sentence = request message
    print("client address: " + str(addr))
    print("IP: " + ip + ", Port: " + str(port))
    print("request sentence/message: \n" + str(sentence))
    
    string_list = sentence.split(' ') # Split request from spaces
    method = string_list[0]
    requestFile = string_list[1]
    print("method: " + method) #method is usually GET in this project
    print("requestFile: " + requestFile) #requestFile is the entered request eg: / or /.png ...etc
    
        
    #if the request is nothing or "/" or "/ar"  or "/en"   
    if requestFile == "" or requestFile == "/" or requestFile == "/en" or requestFile == "/ar" or requestFile.endswith(".html") : 
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        if requestFile == "/ar" :
            htmlFile = open("main_ar.html", "rb") 
        else :
            htmlFile = open("main_en.html", "rb") 
        connectionSocket.send(htmlFile.read())
        htmlFile.close()

    #if the request is an .css file  
    elif requestFile.endswith(".css"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css\r\n".encode())
        connectionSocket.send("\r\n".encode())
        cssFile = open("style.css", "rb") 
        connectionSocket.send(cssFile.read()) 
        cssFile.close()

    #if the request is an .png file  (image)
    elif requestFile.endswith(".png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: Image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        image = open("bzulogo1.png", "rb") 
        connectionSocket.send(image.read())
        image.close()

    #if the request is an .jpg file  (image)        
    elif requestFile.endswith(".jpg") : 
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: Image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        if requestFile == "/pic1.jpg":
            image = open("pic1.jpg", "rb") 
        else:
            image = open("pic2.jpg", "rb") 
        connectionSocket.send(image.read())
        image.close()
        
    #if the request is to redirect to google or cnn or bzu's website
    elif requestFile == "/go" or requestFile == "/cn" or requestFile == "/bzu":
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode()) 
        connectionSocket.send("HTTP/1.0 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())

        if requestFile == "/go":
            connectionSocket.send("location:http://www.google.ps/ \r\n".encode())
        elif requestFile == "/cn":
            connectionSocket.send("location:http://edition.cnn.com/ \r\n".encode()) 
        elif requestFile == "/bzu":
            connectionSocket.send("location:http://www.birzeit.edu/ar \r\n".encode()) 
        
    #if the request is wrong or the file doesn't exist    
    else: 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        htmlFile=('<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta http-equiv="X-UA-Compatible" content="ie=edge"> <title>Error</title> <style> html{ --color1: #161853; --color2: #292C6D; --color3: #FAEDF0; --color4: #EC255A; } body{ background-color: var(--color3); } .cen{ margin: 130px 14px; } h1{ color: var(--color1); text-transform: uppercase; font-size: 60px; } section{ margin: 55px 30px; } h2{ padding-bottom: 15px; } p{ color: var(--color2); } </style> </head> <body> <center class="cen"> <h1>ERROR 404</h1> <h2 class="h22"> Page Not Found -_-</h2> <hr> <section > <h2 style= "font-weight: bold; color:red;">The File Is Not Found</h2> <p style= "font-weight: bold;">Doha Hmeid - 1190120</p> <p style= "font-weight: bold;">Dima Taqatqa - 1191818</p> </section> <hr> <h3>IP: ' + str(ip) + '\n Port: ' + str(port) +' </h3> </center> </body></html>')
        connectionSocket.send(htmlFile.encode('utf'))
     
    connectionSocket.close()
    
    