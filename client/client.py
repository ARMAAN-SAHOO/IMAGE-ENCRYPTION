import socket
import os
import combine as C
# Function to send file data over socket
def send_file_data(filename, client_socket):
    with open(filename, "rb") as f:
        # Read the file data in chunks
        while True:
            data = f.read(4096)
            if not data:
                break
            client_socket.sendall(data)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port
server_host = '172.22.9.151'  # Replace with the actual IP address of the server
server_port = 12345

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}")

    # List of image filenames to send
    filenamesCaptured = ["images/image_0.png","images/image_1.png","images/image_2.png"] 

    #Encryption
    filenames=C.to_process(filenamesCaptured)
    num_images = len(filenames)

    

    # Send the number of images to the server
    client_socket.send(num_images.to_bytes(4, byteorder='big'))

    # Send each image file to the server
    for filename in filenames:
        # Get the size of the image file
        file_size = os.path.getsize(filename)

        # Send the size of the image file to the server
        client_socket.send(file_size.to_bytes(4, byteorder='big'))

        # Send the image file data to the server
        send_file_data(filename, client_socket)
        print(f"Sent {filename} ({file_size} bytes) to the server")

    print("All images sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket connection
    client_socket.close()
