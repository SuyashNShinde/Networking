import socket

HOST = "127.0.0.1"   # localhost
PORT = 5000          # any free port

def main():
    # 1. Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind
    s.bind((HOST, PORT))

    # 3. Listen
    s.listen(1)
    print("Server listening on", (HOST, PORT))

    # 4. Accept one client
    conn, addr = s.accept()
    print("Connected by", addr)

    # 5. Echo loop
    while True:
        data = conn.recv(1024)          # receive from client
        if not data:
            break                       # client closed connection
        print("From client:", data.decode())
        conn.sendall(data)              # send back same data (echo)

    conn.close()
    s.close()

if __name__ == "__main__":
    main()


