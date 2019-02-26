dictOperaciones = {1:'Suma' , 2:'Resta' , 3:'Mutliplicación' , 4:'Division' , 5:'Potencia'}

def modoOperacion():
    print('Escoga entre las siguientes operaicones: ')
    for key in dictOperaciones:
        print(str(key)+'. '+dictOperaciones[key])

    op = input('Introduzca la operación: ')
    try:
        op = int(op)
        if op < 1 or op > 5:
            print('Operacion desconocida')
            return -1
        else:
            return op
    except ValueError:
        print('Operación incorrecta')
        return -1


def realizarOperacion(operando1, operando2, operacion):
    if op == 1:
        print('La suma de ' + str(num1) + ' y ' + str(num2) + ' es igual a ' + str(operando1 + operando2))
    elif op == 2:
        print('La resta de ' + str(num1) + ' y ' + str(num2) + ' es igual a ' + str(operando1 - operando2))
    elif op == 3:
        print('La multiplicación de ' + str(num1) + ' y ' + str(num2) + ' es igual a ' + str(operando1 * operando2))
    elif op == 4:
        if num2 == 0:
            print('División erronea')
        else:
            print('La división de ' + str(num1) + ' y ' + str(num2) + ' es igual a ' + str(operando1 / operando2))
    elif op == 5:
        print('La potencia de ' + str(num1) + ' y ' + str(num2) + ' es igual a ' + str(operando1 ** operando2))


op = modoOperacion()
if op != -1:
    num1 = input('Introduzca un número: ')
    num2 = input('Introduzca otro número: ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        realizarOperacion(num1,num2,op)
    except ValueError:
        print('Operandos introducios son erroneos')

