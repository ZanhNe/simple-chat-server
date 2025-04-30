# 🧩 Simple Multi-Client Chat Server (Python TCP Socket)

This is a simple text-based chat application built with Python using raw TCP sockets.  
It allows multiple clients to connect to a central server and exchange messages in real-time via the terminal.
Server with Python
Client with Golang (power of concurrency)

---

## 🧠 Features

- ✅ Multi-client support via threads (each client gets its own thread)
- ✅ Server-side broadcast of incoming messages to all connected clients
- ✅ Clean shutdown and handling of disconnected clients
- ✅ Plain-text interface
- ✅ Minimal dependencies — built using only Python standard library and Golang

---

## 📚 Learning Goals

This project is designed for educational purposes, especially for those learning:

- Low-level **network programming** using `socket`
- How **TCP connections** work
- How to implement **multi-threaded** servers
- Message broadcasting & client session management

---

## 🚀 Getting Started

### 📦 Requirements

- Python 3.x
- No external libraries required

- Golang 1.18
- No external libraries required

### 🖥 Run the Server

```bash
cd server
python server.py
```

### 🖥 Run the Client

- You should split 2 terminal or more to test multi-client

```bash
cd client
go run client.go
```
