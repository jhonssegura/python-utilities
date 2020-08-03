import threading
import time

def hola_mundo(nombre):
    
    time.sleep(5)
    print("Hola Mundo " + nombre)

def segundo_hilo(prueba):

    print("Segundo hilo "+ prueba)

if __name__ == '__main__':
    thread = threading.Thread(target=hola_mundo, args=("Jhon",))
    thread.start()
    thread2 = threading.Thread(target=segundo_hilo, args=("Salas",))
    thread2.start()

    print("Hilo principal")