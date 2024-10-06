from application.db.people import get_employees
from application.salary import calculate_salary


from box import box

if __name__ == '__main__':

    get_employees('Никита', 'Добров-Рыжов')
    calculate_salary('245 000')
    box()