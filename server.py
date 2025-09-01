#Basic web server with python -Burak "paradass" Görez

import os
import socket
import argparse
import threading

class Server():
    @staticmethod
    def return_page(route:str,url:str) -> str:
        head = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        try:
            if url == "/":
                url += "index.html"
            with open(route + url,"r") as file:
                return head + file.read()
        except:
            return head + "<h1>404 Error!</h1>"
    
    @staticmethod
    def return_icon(route:str):
        head = "HTTP/1.1 200 OK\r\nContent-Type: image/x-icon\r\n\r\n"
        try:
            with open(route+"/favicon.ico","rb") as file:
                return head.encode() + file.read()
        except:
            return None

    def serv(self,route:str,conn:socket.socket,adr):
        request:str = conn.recv(1024).decode()
        request = request.split("\n")[0]
        url:str = request.split(" ")[1]

        if "favicon.ico" in url:
            result = self.return_icon(route)
            if result != None:
                conn.sendall(result)
        else:
            print(f"\033[31mConn:\033[0m{adr}")
            print(f"\033[34mRequest:\033[0m{request}")
            print(f"\033[32mUrl:\033[0m{url}\n")
            conn.sendall(self.return_page(route,url).encode())
        conn.close()
        
    def listen(self,route:str,port:int):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(("",port))
        server_socket.listen()
        print(f"\033[33mServer listening on rout:{route} port:{port}\033[0m\n")

        while True:
            conn,adr = server_socket.accept()
            thread = threading.Thread(target=self.serv,args=(route,conn,adr))
            thread.start()

    def start(self):
        parser = argparse.ArgumentParser(description="Socket web server by paradass",add_help=False)
        parser.add_argument("-r","--route",type=str,default=os.path.dirname(os.path.abspath(__file__)),required=False)
        parser.add_argument("-p","--port",type=int,default=80,required=False)

        args = parser.parse_args()
        self.listen(args.route,args.port)

server = Server()
server.start()