
import  socketserver

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request
        conn.sendall(bytes("你好，我是tcp",encoding="utf-8"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes,encoding="utf-8")
            if ret_str == "q":
                break
            conn.sendall(bytes(ret_str+"来自。。。。",encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),Myserver)
    server.serve_forever()