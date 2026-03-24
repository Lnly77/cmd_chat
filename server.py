# CONFLICT VERSION FROM FEATURE BRANCH
import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    print("server is running on port 5000...")
    
    while True:
        client, addr = server.accept()
        data = client.recv(1024).decode('utf-8')
        print(f"message: {data}")
        client.close()


if __name__ == "__main__":
    start_server()