import socket
import threading
import tkinter as tk

HOST = "127.0.0.1"   # Change to server LAN IP
PORT = 5000

# Socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# ---------------- UI SETUP ---------------- #
root = tk.Tk()
root.title("NETWORKED WHITEBOARD")

# Grey title bar
title_bar = tk.Frame(root, bg="#555555", height=50)
title_bar.pack(fill="x")


# --- Blinking LIVE Indicator --- #

live_frame = tk.Frame(title_bar, bg="#555555")
live_frame.place(x=10, y=12)   # Position on the left side

# Red circle (initially ON)
live_dot = tk.Canvas(live_frame, width=20, height=20, bg="#555555", highlightthickness=0)
dot = live_dot.create_oval(5, 5, 15, 15, fill="red")
live_dot.pack(side="left")

# "ON LIVE" text
live_label = tk.Label(
    live_frame,
    text="ON LIVE",
    bg="#555555",
    fg="white",
    font=("Arial", 12, "bold")
)
live_label.pack(side="left", padx=5)

# Blinking function
dot_state = True
def blink():
    global dot_state
    dot_state = not dot_state
    live_dot.itemconfig(dot, fill="red" if dot_state else "#555555")
    root.after(600, blink)

blink()  # Start blinking


# Main title text in center
title_label = tk.Label(
    title_bar,
    text="NETWORKED WHITEBOARD",
    bg="#555555",
    fg="white",
    font=("Arial", 20, "bold")
)
title_label.place(relx=0.5, rely=0.5, anchor="center")


# ----- Canvas (black board) ----- #
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()


last_x, last_y = None, None

def send_draw(x1, y1, x2, y2):
    msg = f"{x1},{y1},{x2},{y2}".encode()
    client.send(msg)

def draw(event):
    global last_x, last_y
    if last_x is None:
        last_x, last_y = event.x, event.y
        return

    canvas.create_line(last_x, last_y, event.x, event.y, fill="white", width=3)
    send_draw(last_x, last_y, event.x, event.y)
    last_x, last_y = event.x, event.y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None


def receive():
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break

            x1, y1, x2, y2 = map(int, data.split(","))
            canvas.create_line(x1, y1, x2, y2, fill="white", width=3)

        except:
            break


thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

root.mainloop()
