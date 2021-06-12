import socket
import os


def listadoDirectorios():

    listado = os.listdir('.')

    data = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
                <html>
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>Listado de directorios para /</title>
                </head>
                <body>
                <h1>Listado de directorios para /</h1>
                <hr>
                <ul>"""
                
    for d in listado:
        data += "<li><a href='"+ d +"'>"+ d + "</a></li>"

    data += """ </ul>
                <hr>
                </body>
                </html>
                """
    return data



def servidor():
    print("[SERVIDOR ARRANCANDO]")

    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mi_socket.bind(('localhost', 9000))
    mi_socket.listen(1)


    print("[SERVIDOR ESCUCHANDO]")
    while True:
        conexion, direccion = mi_socket.accept()
        print(f"[NUEVA CONEXION] {direccion} conectado")
        conexion.recv(1024)

        conexion.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
        conexion.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
        conexion.send(str.encode('\r\n'))
        conexion.sendall(listadoDirectorios().encode())
        
        conexion.close()
        print(f"[CLIENTE DESCONECTADO] {direccion} desconectado")



def main():
    servidor()

if __name__ == '__main__':
    main()
