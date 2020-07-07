import pprint
from initdata import db

for key in db.keys():
    print(key)
    print(db[key])
print(db)
print(pprint.pformat(db))

with open("testdb.db", 'w') as dbfile:
    dbfile.write('db = ' + pprint.pformat(db) + '\n')
    dbfile.close()
