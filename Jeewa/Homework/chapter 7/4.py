name, *l = input('Enter query name and guest list:').split()

if any(name.lower() == in_l.lower() for in_l in l):
    print(f'Welcome, you are on the list {name}')
else:
    print(f'Sorry, you are not on the list {name}')
