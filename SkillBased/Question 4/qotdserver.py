import socket
import threading
import random

# List of quotes
QUOTES = [
    "An apple a day, keep a doctor away. - at clinic poster",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "kadang kala kita terpaksa melepaskan sesuatu yang kita sayang - Kp2023",
    "Learn as if you will live forever, live like you will die tomorrow. — Mahatma Gandhi",
    "seberat dan serumit apepun keadaan, nikmati prosesnya. - Kaypee2023"
]

def handle_client(client_socket):
    random_quote = random.choice(QUOTES)
    client_socket.send(random_quote.encode())
    client_socket.close()

def main():
    host = "0.0.0.0"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("QOTD Server listening on port", port)

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Connection established with", client_addr)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
