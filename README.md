# ✅ **1) Single-Client Echo Server & Client (Python)**

### 📌 **Concept (what to say in viva)**

* Echo server simply **returns back whatever the client sends**.
* It uses **TCP**, so communication is reliable.
* Server steps: **socket → bind → listen → accept → recv → send**.
* Client steps: **socket → connect → send → recv**.

---

## **Server Explanation**

**File: echo_server.py**

```python
s = socket.socket(...)           # Create TCP socket
s.bind((HOST, PORT))             # Attach to IP & port
s.listen(1)                      # Wait for client
conn, addr = s.accept()          # Accept one client
data = conn.recv(1024)           # Receive data
conn.sendall(data)               # Send same data back (echo)
```

### ✔ Viva Points:

* Only **one client** can connect because it accepts a **single connection**.
* Server is **iterative** (not concurrent).
* Program ends when the client disconnects.

---

## **Client Explanation**

**File: echo_client.py**

```python
s = socket.socket(...)
s.connect((HOST, PORT))          # Connect to server
s.sendall(msg.encode())          # Send data
data = s.recv(1024)              # Receive echo
```

### ✔ Viva Points:

* Client initiates connection using **connect()**.
* Communication is **full duplex**, but here it is used for request–response.
* TCP guarantees ordered delivery.

---

---

# ✅ **2) Single-Client Chat Application**

### 📌 Concept for viva:

* Chat = **both client and server send & receive messages**.
* Works like WhatsApp but only between **1 server and 1 client**.
* Sequence: **client sends → server replies → repeat**.

### Server Explanation

```python
data = conn.recv(1024)           # Receive client's message
reply = input("You: ")           # Server types a reply
conn.sendall(reply.encode())     # Reply sent back
```

### ✔ Viva Points:

* This is a **synchronous chat** (turn-by-turn).
* Both sides wait for each other.
* Uses `recv()` and `sendall()` repeatedly.

---

### Client Explanation

```python
msg = input("You: ")
s.sendall(msg.encode())          # Send to server
data = s.recv(1024)              # Receive server reply
```

### ✔ Viva Points:

* Client also performs **send → receive** in a loop.
* Terminates on typing **exit**.

---

---

# ✅ **3) Multi-Client Server (Concurrent Server using Threads)**

### 📌 Concept for viva:

* One server handles **many clients at the same time**.
* Uses **threads** so each client gets its own execution path.
* This is a **concurrent server**, not iterative.

---

## Server Explanation

```python
threading.Thread(target=handle_client, args=(conn, addr)).start()
```

This line creates a **new thread** for each client.

### Inside `handle_client()`:

```python
data = conn.recv(1024)   # Receive from one client
conn.sendall(data)       # Respond only to that client
```

### ✔ Viva Points:

* Threaded server = multiple clients simultaneously.
* `listen()` remains active for new clients even during communication.
* Each client is independent; one client crashing **won’t affect others**.

---

## Client Explanation

Client is same as echo client, because server is multi-client.

### ✔ Viva Points:

* Multiple clients run the same file.
* Client is unaware that server is multi-client.

---

---

# ✅ **4) Two Servers – One Client**

### 📌 Concept for viva:

* Client chooses which server to connect to.
* Servers run on different **ports**.
* Client makes a decision: **port 6000** or **port 6001**.

### Server 1

```python
s.bind(("127.0.0.1", 6000))
```

### Server 2

```python
s.bind(("127.0.0.1", 6001))
```

### Client

```python
choice = int(input("1 or 2? "))
if choice == 1:
    port = 6000
else:
    port = 6001
s.connect((HOST, port))
```

### ✔ Viva Points:

* Client is acting as a **service selector**.
* Both servers work independently.
* Servers do not communicate with each other.

---

---

# ✅ **5) Multi-Client Chat (Broadcast Chat)**

(*If needed, optional explanation — used in many CN labs*)

### 📌 Concept

* Server receives a message from one client and **broadcasts** it to all other clients.
* This is how a real chatroom works.

### Viva points:

* Uses a **list of connected clients**.
* When one client sends a message → server loops and sends to all others.
* This is **concurrent** + **broadcasting**.

---

# 🎯 IMPORTANT VIVA QUESTIONS + READY ANSWERS

### **Q1. Difference between iterative and concurrent server?**
**Answer:**

* Iterative server handles **one client at a time**.
* Concurrent server handles **multiple clients simultaneously** using threads/processes.

---

### **Q2. Why do we use threads for multi-client servers?**
**Answer:**
To allow each client to communicate independently without blocking others.

---

### **Q3. What is the purpose of bind()?**
**Answer:**
It assigns the server’s socket to a **specific IP address and port**.

---

### **Q4. What is the role of listen()?**
**Answer:**
It tells the OS that the socket is a **server socket** waiting for incoming connections.

---

### **Q5. What happens at accept()?**
**Answer:**
Accept creates a **new socket** dedicated to a specific client.

---

### **Q6. Why use sendall() instead of send()?**
**Answer:**
`sendall()` ensures **all bytes** are transmitted.

---

### **Q7. What is the difference between TCP and UDP?**
**Answer:**
TCP = reliable, connection-oriented
UDP = fast, connectionless, no guarantee.


QAs:-
Q1. Difference: Iterative vs Concurrent Server
Ans:
Iterative → handles one client at a time.
Concurrent → handles multiple clients using threads or processes.

Q2. Why use threads in multi-client server?
Ans:
Each client gets its own thread → non-blocking → simultaneous communication.

Q3. What does bind() do?
Ans:
Assigns IP and port to server’s socket.

Q4. What does listen() do?
Ans:
Puts the socket in passive mode, waiting for clients.

Q5. What does accept() do?
Ans:
Creates a new socket for each connected client.

Q6. Why use sendall() instead of send()?
Ans:
sendall() ensures all bytes are delivered reliably.

Q7. What protocol does TCP use internally?
Ans:
Three-way handshake (SYN → SYN-ACK → ACK).

Q8. Why do we use port numbers?
Ans:
To identify specific applications/services on a machine.

Q9. What is the maximum size of data in recv()?
Ans:
1024 bytes (as defined by programmer, not fixed by protocol).

Q10. What is full-duplex communication?
Ans:
Both sides can send and receive simultaneously (TCP is full duplex).
If you want, I can now prepare a **one-page cheat sheet** for tomorrow’s practical   or
I can also give **expected viva questions with answers for your examiner**.
