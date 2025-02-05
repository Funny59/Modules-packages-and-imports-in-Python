from datetime import datetime
import sys

sys.path.append('./application')
sys.path.append('./application/db')

from salary import calculate_salary
from people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.today())