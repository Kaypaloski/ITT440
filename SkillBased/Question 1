import socket

def main():
    host = "izani.synology.me"
    port = 8443
    studentID = "2021603372"

    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        print(f"Connected to {host} at port {port}")

        client_socket.sendall(studentID.encode())
        respon=client_socket.recv(1024)
        print(respon.decode())

        # Close the connection
        client_socket.close()

        print("Connection closed.")
    except socket.error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

