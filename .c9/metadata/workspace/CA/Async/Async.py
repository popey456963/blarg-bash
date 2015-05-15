{"filter":false,"title":"Async.py","tooltip":"/CA/Async/Async.py","undoManager":{"mark":83,"position":83,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":44,"column":21},"action":"insert","lines":["import socket","import threading","import socketserver","","class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):","","    def handle(self):","        data = str(self.request.recv(1024), 'ascii')","        cur_thread = threading.current_thread()","        response = bytes(\"{}: {}\".format(cur_thread.name, data), 'ascii')","        self.request.sendall(response)","","class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):","    pass","","def client(ip, port, message):","    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)","    sock.connect((ip, port))","    try:","        sock.sendall(bytes(message, 'ascii'))","        response = str(sock.recv(1024), 'ascii')","        print(\"Received: {}\".format(response))","    finally:","        sock.close()","","if __name__ == \"__main__\":","    # Port 0 means to select an arbitrary unused port","    HOST, PORT = \"localhost\", 0","","    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)","    ip, port = server.server_address","","    # Start a thread with the server -- that thread will then start one","    # more thread for each request","    server_thread = threading.Thread(target=server.serve_forever)","    # Exit the server thread when the main thread terminates","    server_thread.daemon = True","    server_thread.start()","    print(\"Server loop running in thread:\", server_thread.name)","","    client(ip, port, \"Hello World 1\")","    client(ip, port, \"Hello World 2\")","    client(ip, port, \"Hello World 3\")","","    server.shutdown()"]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":39,"column":4},"end":{"row":40,"column":0},"action":"insert","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":13},"end":{"row":40,"column":14},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":15},"end":{"row":40,"column":16},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":16},"end":{"row":40,"column":17},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":17},"end":{"row":40,"column":18},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":18},"end":{"row":40,"column":19},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":19},"end":{"row":40,"column":20},"action":"insert","lines":["1"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":20},"end":{"row":40,"column":21},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":21},"end":{"row":40,"column":22},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":22},"end":{"row":40,"column":23},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":23},"end":{"row":40,"column":24},"action":"insert","lines":[":"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":4},"end":{"row":41,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"remove","lines":["1"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["+"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":43},"end":{"row":41,"column":44},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":44},"end":{"row":41,"column":45},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":45},"end":{"row":41,"column":46},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":42,"column":0},"end":{"row":43,"column":37},"action":"remove","lines":["    client(ip, port, \"Hello World 2\")","    client(ip, port, \"Hello World 3\")"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":49},"end":{"row":42,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":40,"column":21},"end":{"row":40,"column":22},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":26},"end":{"row":41,"column":47},"action":"remove","lines":["Hello World \" + str(i"]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["A"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["w"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":42},"end":{"row":41,"column":43},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":46},"end":{"row":41,"column":47},"action":"remove","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":41,"column":45},"end":{"row":41,"column":46},"action":"remove","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":46},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"remove","lines":["n"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["s"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"remove","lines":[" "]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":42,"column":34},"end":{"row":42,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1424194198808,"hash":"502a622bd90e51fe960260a46be6f4f6d35f4003"}