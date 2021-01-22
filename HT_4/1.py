'''
1. Створіть функцію, всередині якої будуть записано список із п'яти
користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових
   (<username> та <password>) і третій - необов'язковий параметр <silent>
   (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> -
       функція вертає <False>, інакше (<silent> == <False>) - породжується
       виключення LoginException
'''
class LoginException (Exception):
    pass

def func_1(**a):
    b={'qwe':'ewq','asd':'dsa','zxc':'cxz','wer':'rew','sdf':'fds'}
    z=input("Якщо хочете побачити список із 5 користувачів (ім'я та пароль), введіть 'y':")
    if z=='y':
        print(b)
    a = {
    'username': input("Введіть ім'я (username): "),
    'password': input('Введіть пароль (password): '),
    'silent': input("Введіть True(необов'язково), за замовчуванням залишається - 'False': ")
    }
    if not a['silent']:
        a['silent'] = 'False'
    

    if a['silent']=='True' or a['silent']=='False':
        if a['username'] in b and b[a['username']]==a['password']:
            print(True)
            return(True)
        if a['silent']=='True':
            if a['username'] not in b or b[a['username']]!=a['password']:
                print(False)
                return(False)
        if a['silent']=='False':
            if a['username'] not in b or b[a['username']]!=a['password']:
                raise LoginException('Це помилка')
    else:
        print('Ви ввели неправильно True/False, спробуйте ще раз')
func_1()
