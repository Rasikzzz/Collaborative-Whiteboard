import socket
import threading

HOST = '0.0.0.0'   # Listen on all network interfaces
PORT = 5000

clients = []


def broadcast(message, connection):
    """Send drawing data to all connected clients except sender."""
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            broadcast(data, conn)

        except:
            break

    conn.close()
    if conn in clients:
        clients.remove(conn)
    print(f"[DISCONNECTED] {addr}")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    start_server()
