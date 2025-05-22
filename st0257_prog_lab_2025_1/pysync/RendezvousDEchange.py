# pysync/RendezvousDEchange.py
import threading

class RendezvousDEchange:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.partner_value = None
        self.thread_ready = False

    def echanger(self, value):
        with self.condition:
            if not self.thread_ready:
                # First thread arrives
                self.partner_value = value
                self.thread_ready = True
                self.condition.wait()  # Wait for partner
                return self.partner_value
            else:
                # Second thread arrives
                return_value = self.partner_value
                self.partner_value = value
                self.thread_ready = False
                self.condition.notify()  # Notify partner
                return return_value

    def sync(self, thread_id):
        with self.lock:
            if thread_id == 1:
                self.thread1_arrived = True
                while not self.thread2_arrived:
                    self.condition.wait()
                self.thread2_arrived = False
            else:
                self.thread2_arrived = True
                self.condition.notify_all()
                while not self.thread1_arrived:
                    self.condition.wait()
                self.thread1_arrived = False