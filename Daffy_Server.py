import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    print(f'Listening on port {SERVER_PORT} ...')

    while True:
        # Wait for client connections
        client, client_address = s.accept()
        print(f"{client_address} has coonnected!")

        # Get the client request
        with client as c:
            request = c.recv(1024).decode()
            print(request)

            # Send HTTP response
            response = """ \n
<!DOCTYPE html>
<html>
<body style="background-color:powderblue;">
<style>
h1 {text-align: center;}
p {text-align: center;}
</style>

<p>
<img src="https://i.pinimg.com/originals/da/47/68/da47680f49a6570c11ea61318e96cb5c.png" alt="Daffy" width="150" height="220">
</p>

<h1 style="color:teal" "font-family:'Courier New'">Welcome to Daffy's Website!</h1>

</body>
</html>

"""
            #send response to client
            c.sendall("HTTP/1.1 200 OK".encode())
            c.sendall(response.encode())
