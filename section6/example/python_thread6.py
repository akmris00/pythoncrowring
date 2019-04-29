#일정 시간 간격으로 반복 실행
import time
import threading

def thread_run():
    print('----------', time.ctime(), '----------')
    #개발 하고자 하는 코드 작성
    #########################
    for i in range(1, 1001):
        print('Threading running - ', i)

    threading.Timer(2.5, thread_run).start() # 재귀함수

thread_run()
