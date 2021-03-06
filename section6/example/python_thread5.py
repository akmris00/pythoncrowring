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


#데몬 쓰레드(옵션 생략시 기본 쓰레드)
t1 = threading.Thread(name="service-1", target=worker1)
t2 = threading.Thread(name="service-2", target=worker2, daemon=True)
t3 = threading.Thread(target=worker1, daemon=True)

if __name__ == "__main__":
    t1.start()
    t2.start()
    t3.start()

    #join 메소드 호출로 쓰레드 종료시 까지 대기
    t1.join() #join() 시간 동안 대기
    t2.join()
    t3.join()
