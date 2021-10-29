from dataclasses import dataclass
from typing import List

EMPLOYEES: List['Employee'] = []
FIRST_TIME = True

@dataclass
class Employee:
    __slots__ = ('name_surname', 'name', 'surname', 'empl_id', 'username', 'password')
    name_surname: str
    empl_id: int
    
    def __post_init__(self) -> None:
        self.name, self.surname = map(lambda x: x.lower(), self.name_surname.split(maxsplit=1))
        self.username = f'{self.name}.{self.surname[0]}'
        self.password = f'{self.name[1].lower()}{self.name[3].upper()}{self.name[2].upper()}{len(self.name_surname)}{self.name[4].lower()}'
        EMPLOYEES.append(self)

def main_menu() -> int:
    global FIRST_TIME
    if FIRST_TIME:
        print('========================Welcome Employee System Program=========================')
        FIRST_TIME = False
    else:
        print('================================================================================')
    print('1 Register Employee')
    print('2 Delete Employee')
    print('3 Show Data Employee')
    print('4 Exit Program')
    option = int(input('Please select menu[1-3] : '))
    if 4 >= option >= 1:
        return option
    print('Incorrect menu!!')
    return 0

def menu_one() -> Employee:
    print('================================================================================')
    print('===============================REGISTER EMPLOYEE'.replace('=', ' '))
    print('================================================================================')
    name_surname = input('Enter Name Surname : ')
    text = 'Enter ID card [13 digits] : '
    while True:
        iden_num = input(text)
        text = 'Enter ID card : '
        if len(iden_num) == 13:
            print('Register Complete')
            Employee(name_surname, int(iden_num))
            return
        print('Invalid ID card')

def menu_two() -> None:
    global EMPLOYEES
    print('================================================================================')
    print('================================DELETE EMPLOYEE'.replace('=', ' '))
    print('================================================================================')
    while True:
        name = input('Enter name employee to delete : ')
        for employee in EMPLOYEES:
            if name.lower() == employee.name.lower():
                print('Delete Complete')
                EMPLOYEES.remove(employee)
                return
        print('Invalid name !!')

def menu_three() -> None:
    global EMPLOYEES
    print('================================================================================')
    print('================================DELETE EMPLOYEE'.replace('=', ' '))
    print('================================================================================')
    print(f'{"No.".ljust(8)}{"Name".ljust(13)}{"Surname".ljust(19)}{"Username".ljust(13)}{"Password".ljust(13)}{"ID Card".ljust(14)}')
    for i, employee in enumerate(EMPLOYEES, 1):
        print(f'{str(i).ljust(8)}{employee.name.ljust(13)}{employee.surname.ljust(19)}{employee.username.ljust(13)}{employee.password.ljust(13)}{str(employee.empl_id).ljust(14)}')

def menu_four() -> bool:
    print('==================================Exit Program==================================')
    return False

def main():
    running = True
    while running:
        good_result = False
        while not good_result:
            option = main_menu()
            good_result = bool(option)
        if option == 1:
            menu_one()
        elif option == 2:
            menu_two()
        elif option == 3:
            menu_three()
        else:
            running = menu_four()

if __name__ == '__main__':
    main()
