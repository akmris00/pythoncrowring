#로깅 패키지
#정말 중요함
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s (%(threadName)-8s) %(message)s]',
)

def worker1():
    logging.debug('starting')
    time.sleep(0.5)
    logging.debug('exit')

def worker2():
    logging.debug('starting')
    time.sleep(0.5)
    logging.debug('exit')


t1 = threading.Thread(name="service-1", target=worker1)
t2 = threading.Thread(name="service-2", target=worker2)
t3 = threading.Thread(target=worker1)

t1.start()
t2.start()
t3.start()
