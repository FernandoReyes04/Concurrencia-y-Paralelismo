import threading
import time

# Creamos un semáforo que inicialmente tiene el valor 1 (un único acceso permitido a la vez).
sem = threading.Semaphore(1)

# Esta es la función que representará la región crítica
def region_critica(id_hilo):
    # Intentamos entrar en la región crítica
    print(f"Hilo {id_hilo} intentando entrar en la región crítica.")
    sem.acquire()  # Esperamos si otro hilo ya está en la región crítica
    print(f"Hilo {id_hilo} dentro de la región crítica.")
    
    # Simulamos que el hilo realiza alguna operación en la región crítica
    time.sleep(2)  # Este sleep es solo para simular que toma tiempo realizar la operación
    
    # Terminamos y salimos de la región crítica
    print(f"Hilo {id_hilo} saliendo de la región crítica.")
    sem.release()  # Liberamos el semáforo para que otro hilo pueda entrar

# Esta función crea varios hilos que intentan acceder a la región crítica
def crear_hilos(num_hilos):
    hilos = []
    for i in range(num_hilos):
        hilo = threading.Thread(target=region_critica, args=(i,))
        hilos.append(hilo)
        hilo.start()

    # Esperamos a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    num_hilos = 10  # Número de hilos que intentarán acceder a la región crítica
    crear_hilos(num_hilos)
