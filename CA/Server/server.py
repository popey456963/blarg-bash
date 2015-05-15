from __main__ import * # So we get the function we require.
from parse import *
import socketserver, socket # Some socket imports for the server to use

print("Server.py Import: Complete") # Let the user know that this file has actually been imported

def serve(ip, port): # Wrapped in a function so that it can be easily called

    class MyTCPHandler(socketserver.BaseRequestHandler): # Class called MyTCPHandler
    
        def handle(self): # Another function that requests data, and then sends it back
        
            self.data = self.request.recv(1024) # Ask for data
            self.request.sendall(self.data) # Send it back
            print(self.data) # Print it out
            Parser(self.data) # Let main know data has been received
            
    print("Server up and running!") # Let the user know their server is running
    server = socketserver.TCPServer((ip, port), MyTCPHandler) # Create the server
    server.serve_forever() # Server forever, self explanatory