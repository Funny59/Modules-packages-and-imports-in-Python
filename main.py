from datetime import datetime
import sys
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.today())
