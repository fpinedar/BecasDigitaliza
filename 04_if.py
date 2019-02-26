
num = input('Introduce un número: ')

try:
    num = int(num)
    if type(num) == int:
        if int(num) < 20:
            print('Número '+str(num)+' es menor que 20')
        elif 20 <= int(num) < 40:
            print('Número '+str(num)+' esta entre 20 y 39')
        elif 40 <= int(num) < 60:
            print('Número '+str(num)+' esta entre 40 y 59')
        elif int(num) >= 60:
            print('Número '+str(num)+' es mayor o igual que 60')
except ValueError:
    print('El número introducio no es valido')
