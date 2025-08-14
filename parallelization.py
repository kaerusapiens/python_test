import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def worker1():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

def worker2():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1,daemon=True)
        t.start()
        threads.append(t)
    for thread in threads:
        
        thread.join()


    # t1 = threading.Thread(target=worker1,daemon=True)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # t1.join()