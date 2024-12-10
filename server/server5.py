import socket
import cv2
import numpy as np

# Function to receive and process images
def startserver():
    def receive_images(client_socket,img_no):
        try:
            # Receive the number of images to expect
            num_images_bytes = client_socket.recv(4)
            num_images = int.from_bytes(num_images_bytes, byteorder='big')

            for i in range(num_images):
                # Receive the image size
                image_size_bytes = client_socket.recv(4)
                image_size = int.from_bytes(image_size_bytes, byteorder='big')
            
                # Receive the image data in chunks
                image_data = b''
                remaining_size = image_size
                while remaining_size > 0:
                    chunk = client_socket.recv(min(4096, remaining_size))
                    if not chunk:
                        break
                    image_data += chunk
                    remaining_size -= len(chunk)
                # Convert the received bytes back to a NumPy array
                image_array = np.frombuffer(image_data, dtype=np.uint8)

                # Reshape the NumPy array to the original image shape
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                print(image.shape)
                cv2.imshow("Received Image"+str(img_no+1), image)
                cv2.imwrite("ReceivedImage"+str(img_no+1)+".png", image)
                
                img_no+=1
                #cv2.waitKey(5000)  # Show each image for 1 second
            return img_no 
        except Exception as e:
            print("Error receiving images:"+e)

        finally:
            cv2.destroyAllWindows()
        
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine IP address or use a specific IP if available
    host = '172.22.9.151'  # Replace with the actual IP address of the server
    port = 12345

    # Bind to the port
    server_socket.bind((host, port))

    # Wait for client connection
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")
    img_no=0
    while True:
        # Accept incoming client connection
        client_socket, addr = server_socket.accept()
        print(f"Got connection from {addr}")

        try:
            # Receive and process images from the client
            img_no=receive_images(client_socket,img_no)
            server_socket.close()
        except Exception as e:
            print(f"Error with client connection: {e}")

        finally:
            client_socket.close()
            return img_no