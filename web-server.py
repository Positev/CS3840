import socket

class WebServer:
    def __init__(self, port_number = 6994):
        self.socket_connection = socket.socket(AF_INET, SOCK_STREAM)
        self.port_number = port_number

    def run(self):
        self.socket_connection.bind('', self.port_number)

        while True:
            message = self.socket_connection.recv(1024)



    def stop(self):
        self.socket_connection.close()


    def serve_static_resource(self, resource_file_path):
        try:
            with open(resource_file_path, 'r') as output_file:
                output_data = output_file.read()

            self.socket_connection.send('HTTP/1.0 200 OK\r\n\r\n'.encode())

            for i in range(len(output_data)):
                self.socket_connection.send(output_data[i].encode())
            
            self.socket_connection.send('\r\n'.encode())
        
        except OSError as e:
            self.socket_connection.send('404 Not Found'.encode())  
        
        except socket.error as e:
            pass

                
