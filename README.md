# 📌 Collaborative Whiteboard (Python + Sockets + Tkinter)

A real-time collaborative whiteboard application built using Python, Socket Programming, Threads, and Tkinter.  
Multiple clients connected to a server can draw on a shared canvas — every stroke is synchronized instantly across all devices.

---

## ✨ Features
- Real-time shared drawing across multiple clients  
- TCP client–server communication  
- Multithreaded server  
- Tkinter GUI  
- Blinking "ON LIVE" status indicator  
- Smooth broadcast of drawing data  

---

## 🗂 Project Structure
- server.py → Handles client connections and broadcasting  
- client.py → GUI drawing application  
- README.md  

---

## 🛠 Tech Stack
- Python 3  
- socket  
- threading  
- tkinter  

---

## 🚀 How It Works

### Server (server.py)
- Accepts TCP connections  
- Listens for drawing data  
- Broadcasts received drawing commands to all clients except the sender  

### Client (client.py)
- Connects to server  
- User draws on a canvas  
- Sends line coordinates to server  
- Renders other clients' strokes on its canvas  
- Shows a blinking ON LIVE indicator  

---

## 📌 Installation

1. Clone the repository  
   git clone https://github.com/rasikzzz/Collaborative-Whiteboard.git  
   cd Collaborative-Whiteboard  

2. Requirements  
   Only Python 3 is required. Tkinter is preinstalled in most systems.

---

## ▶️ Run the Server
python server.py  

You should see:  
[SERVER STARTED] Listening on 0.0.0.0:5000

---

## ▶️ Run the Client

Edit the HOST value at the top of client.py.  
Default: HOST = "127.0.0.1"  

Replace it with your server machine’s LAN IP, for example:  
HOST = "192.168.1.10"  

Then run:  
python client.py  

Use multiple devices for collaborative drawing.

---

## 🎨 Usage
- Click and drag on the black canvas to draw  
- The drawing syncs across all connected clients  
- The red blinking dot shows live activity  

---

## 🔮 Future Improvements
- Eraser tool  
- Brush size control  
- Color picker  
- Save canvas as PNG  
- Undo/Redo  
- Chatbox  
- Browser (web) client  

---

## 🤝 Contributing
Pull requests are welcome! Fork the repository and add features.

---

## 📜 License
This project is open-source and free to modify.
