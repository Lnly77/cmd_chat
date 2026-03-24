import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    print("server is running on port 5000...")

    while True:
        client, addr = server.accept()
        raw_data = client.recv(1024).decode('utf-8')
        if ":" in raw_data:
            name, msg = raw_data.split(":", 1)
            print(f"[{name.strip()}]: {msg.strip()}")
        client.close()

if __name__ == "__main__":
    start_server()
