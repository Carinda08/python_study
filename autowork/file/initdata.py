names =['name', 'pay', 'age', 'work']
value1 = ['John Carl', 10000, 32, 'hardware']
value2 = ['Tom King', 20000, 34, 'software']
value3 = ['Bob Smith', 21000, 21, 'manager']

db = {}
db['john'] = dict(zip(names, value1))
db['tom'] = dict(zip(names, value2))
db['bob'] = dict(zip(names, value3))

if __name__ == '__main__':
    for key in db.keys():
        print(key, '->', db[key])
