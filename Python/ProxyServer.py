import socket
import sys
from threading import Thread as thread

try:
    listening_port = int(input("[*] Enter listening port number: "))
except KeyboardInterrupt:
    print("\n[*] User Requested An Interrupt...")
    print("\n[*] Application Exiting.")
    sys.exit()

max_conn = 5
buffer_size = 8192


def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', listening_port))
        s.listen(max_conn)
        print("[*] Initializing Sockets... Done")
        print("[*] Sockets binded successfully...")
        print("[*] Server started at [ %d] " % listening_port)
    except:
        print("[*] Unable to initialize Sockets...")
        sys.exit(2)

    while(True):
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
        except KeyboardInterrupt:
            s.close();
            print("[*] Proxy server shutting down...")
            sys.exit(1)

    s.close()


def conn_string(conn, data, addr):
    try:
        first_line = data.split("\n")[0]
        url = first_line.split(' ')[1]
        http_pos = url.find("://")
        if(http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos+3):]

        port_pos = temp.find(":")
        webserver_pos = temp.find("/")

        if(webserver_pos == -1):
            webserver_pos = len(temp)
        webserver = ""
        port = -1

        if(port_pos == -1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]
        proxy_server(webserver, port, conn, addr, data)
    except Exception:
        pass

def proxy_server(webserver, port, conn, addr, data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(data)

        while(True):
            reply = s.recv(buffer_size)

            if(len(reply) > 0):
                conn.send(reply)
                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)
                print("[*] Request Done: %s => %s <=" % (str(addr[0]), str(dar)))
            else:
                break

        s.close()
        conn.close()
    except Exception:
        s.close()
        conn.close()
        sys.exit(1)

start()