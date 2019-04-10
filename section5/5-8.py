import pandas_datareader.data as web
import pandas as pd
import datetime
import sqlite3

#pandas, pandas_datareader 설치
try:
    with sqlite3.connect('c:/Atom/Crowring/section5/databases/sqlite2.db') as conn:
        #조회 시작 & 마감 날짜
        start = datetime.datetime(2018, 2, 1)
        end = datetime.datetime(2018,3,3)

        #google 정보 호출
        gs = web.DataReader('KRX: 090430', 'google', start, end) #아모래퍼시픽 주가 읽기

        print(gs)

        #인텍스 출력
        print(gs.index)

        #컬럼 출력
        print(gs['Open'])

        #Row 출력
        print(gs.ix['2018-03-02'])

        #Index to column
        gs['Date'] = gs.index

        #인덱스 재설정
        gs.index = range(1,(len(gs.index)+1))
pr      print(gs)


finally:
    print("Dataframe SQL work complete!")
