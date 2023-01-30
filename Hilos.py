import threading
import time



class Hilo(threading.Thread):
    def run(self):
        print(f'Inicio de: {self.getName()}')
        time.sleep(0.5)
        print(f'Fin de: {self.getName()}')

if __name__ == '__main__':
    for i in range(4):
        hilo = Hilo(name=f'Hilo {i+1}')
        hilo.start()
        time.sleep(0.1)