#Basic web server with python -Burak "paradass" Görez

import os
import socket
import argparse

class Server():
    @staticmethod
    def return_page(route:str,url:str) -> str:
        head = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        try:
            if url == "/":
                url += "index.html"
            file = open(route + url,"r")
            return head + file.read()
        except:
            return head + "<h1>404 Error!</h1>"

    def listen(self,route:str,port:int):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(("",port))
        server_socket.listen()

        print(f"Server listening on rout:{route} port:{port}\n")

        while True:
            conn,adr = server_socket.accept()
            print(f"Conn:{adr}")

            request:str = conn.recv(1024).decode()
            print(f"Request:{request}")

            try:
                url:str = request.split(" ")[1]
                print(f"Url:{url}\n")

                conn.sendall(self.return_page(route,url).encode())
            except:
                pass
            conn.close()

    def start(self):
        parser = argparse.ArgumentParser(description="Socket web server by paradass",add_help=False)
        parser.add_argument("-r","--route",type=str,default=os.path.dirname(os.path.abspath(__file__)),required=False)
        parser.add_argument("-p","--port",type=int,default=80,required=False)

        args = parser.parse_args()
        self.listen(args.route,args.port)

server = Server()
server.start()