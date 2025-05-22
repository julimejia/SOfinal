from threading import Thread, Lock, Condition
import time

class RendezvousDEchange:
    def __init__(self):
        self.lock = Lock()
        self.condition = Condition(self.lock)  # Corregido: Usando Condition importada
        self.value1 = None
        self.value2 = None
        self.ready = False

    def echanger(self, value, divisor):
        with self.condition:
            if not self.ready:
                # Primer hilo llega
                self.value1 = value
                self.ready = True
                while self.ready:
                    self.condition.wait()
                return self.value2
            else:
                # Segundo hilo llega
                self.value2 = value
                self.ready = False
                self.condition.notify_all()
                return self.value1

def producer(prod_cons, max_value):
    for i in range(max_value + 1):
        prod_cons.put(i)
        time.sleep(0.001)

def consumer(prod_cons, rendezvous, divisor, max_value, name):
    while True:
        value = prod_cons.get()
        if value > max_value:
            break
            
        if value % divisor == 0:
            exchanged = rendezvous.echanger(value, divisor)
            print(f"SWAP: {name} intercambió {value} por {exchanged}")

if __name__ == "__main__":
    print("Sistema iniciado - Solo se mostrarán los swaps")
    
    from queue import Queue
    q1, q2 = Queue(), Queue()
    rdv = RendezvousDEchange()
    
    MAX_3 = 3000
    MAX_5 = 5000
    
    producers = [
        Thread(target=producer, args=(q1, MAX_3)),
        Thread(target=producer, args=(q2, MAX_5))
    ]
    
    consumers = [
        Thread(target=consumer, args=(q1, rdv, 3, MAX_3, "Hilo-3")),
        Thread(target=consumer, args=(q2, rdv, 5, MAX_5, "Hilo-5"))
    ]
    
    for p in producers:
        p.start()
    for c in consumers:
        c.start()
    
    for p in producers:
        p.join()
    
    q1.put(MAX_3 + 1)
    q2.put(MAX_5 + 1)
    
    for c in consumers:
        c.join()
    
    print("Sistema terminado")