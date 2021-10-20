GRADE = {
    key:4-(0.5*i) for i, key in enumerate(['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'])
}


def main():
    print('==============================================================')
    print('***********       Welcome to Grade Calculator      ***********')
    print('==============================================================')
    
    student_id = input('Enter student\'s ID: ')
    student_name = input('Enter student\'s name: ')
    faculty = input('Enter student\'s faculty: ')
    print()
    subjects_number = int(input('Enter Subjects Amount: '))
    sbjs = []
    for i in range(1, subjects_number+1):
        sbj_name = input(f'Enter Subject {i}.: ')
        sbj_cred = input('Enter Credit: ')
        sbj_grade = input('Enter Grade: ')
        sbjs.append([sbj_name, sbj_cred, sbj_grade]) 
    
    print('==============================================================')
    print('|                       Grade Calculator                     |')
    print('==============================================================')
    print(f'Student ID. {student_id}')
    print(f'Name: {student_name}')
    print(f'School: {faculty}')
    print('==============================================================')
    print('|          Subject           |    Credit(s)   |     Grade    |')
    print('==============================================================')
    g = 0
    for name, credit, grade in sbjs:
        if grade == 'w':
            subjects_number -= 1
        else:
            g += int(credit) * GRADE[grade.upper()]
        print('==============================================================')
        print(name, credit, grade)
    
    print('==============================================================')
    print('|'.ljust(1), f'{g/subjects_number:.2f}'.center(20), '|'.rjust(1))
    print('==============================================================')

if __name__ == '__main__':
    main()


