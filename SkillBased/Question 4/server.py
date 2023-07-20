import socket

def convert_to_atm(pressure):
    return pressure * 0.986923

def main():
    host = "0.0.0.0"
    port = 8334

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on port", port)

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Connection established with", client_addr)
        data = client_socket.recv(1024)
        pressure_in_bar = float(data.decode())
        pressure_in_atm = convert_to_atm(pressure_in_bar)
        client_socket.send(str(pressure_in_atm).encode())
        client_socket.close()
        print("Connection closed with", client_addr)

if __name__ == "__main__":
    main()
