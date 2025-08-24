#Basic web server with python -Burak "paradass" Görez

import socket
import argparse

class Server():
    @staticmethod
    def return_page(path:str):
        pass

    def listen(self,route:str,port:int):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind(("",port))
        server_socket.listen()

        print(f"Server listening on port {port}\n")

        while True:
            conn,adr = server_socket.accept()
            print(f"Conn: {adr}")

            request = conn.recv(1024).decode()
            print(f"Request: {request}")

            conn.close()

    def start(self):
        parser = argparse.ArgumentParser(description="#Basic web server with python",add_help=False)
        parser.add_argument("-r","--route",type=str,required=True)
        parser.add_argument("-p","--port",type=int,default=8080,required=False)

        args = parser.parse_args()
        self.listen(args.route,args.port)

server = Server()
server.start()