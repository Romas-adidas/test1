from functions import salary, hello_who

if salary(2,5) != 20:
    print('Error')
if hello_who('Роман') != 'Hello, Роман':
    print('Failed')
else:
    print('success')
if hello_who('Эль примо') != 'Hello, Эль примо':
    print('Failed')
else:
    print('success')
if salary == 20:
    print('norm')

