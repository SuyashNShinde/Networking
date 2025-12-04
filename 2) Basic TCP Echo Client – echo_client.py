import socket

HOST = "127.0.0.1"   # server IP
PORT = 5000          # same as server

def main():
    # 1. Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect to server
    s.connect((HOST, PORT))
    print("Connected to server")

    # 3. Send–receive loop
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        s.sendall(msg.encode())             # send to server

        data = s.recv(1024)                 # receive echo
        if not data:
            break
        print("From server:", data.decode())

    s.close()

if __name__ == "__main__":
    main()
