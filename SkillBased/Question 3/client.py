import socket

def main():
    host = "192.168.149.130"
    port = 8334

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print("Connected to server.")

    try:
        pressure_in_bar = float(input("Enter pressure value in bar: "))
        client_socket.send(str(pressure_in_bar).encode())

        data = client_socket.recv(1024)
        pressure_in_atm = float(data.decode())

        print(f"Pressure in atm: {pressure_in_atm:.4f} atm")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()

