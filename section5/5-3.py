import simplejson as json
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage

#파일 DB 생성
db = TinyDB('c:/Atom/section5/databases/database.db', default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()


# users의 여러가지 조회 방법
#print(users.search(Users.id == 7))
#print(users.search(Users['id'] == 7))
#print(users.search(where('id') == 7))
#print(users.search(Query()['id'] == 7))
#print(users.search(where('address')['zipcode'] == '90566-7771'))
#print(users.search(where('address').zipcode == '90566-7771'))


#고급 쿼리
print(users.search(Users.email.exists()))
print(users.search(Users['email'].exists()))
print(users.search(Users.aaa.exists()))

#NOT
print('NOT', users.search(~(Users.username == 'Antonette')))
print('NOT', users.search(Users.username != 'Antonette'))

#OR
print('OR', users.search((Users.username == 'Antonette') | (Users.username == 'Antonette')))

#AND
print('AND', users.search((Users.username == 'Antonette') & (Users.id == 2)))

#기타 함수
print('len', len(users))
print('len', len(todos))
print('contains', users.contains(Users.username == 'Kamren'))
print('count', users.count(Users.username == 'Kamren'))
