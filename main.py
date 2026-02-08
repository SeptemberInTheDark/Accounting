from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now())


