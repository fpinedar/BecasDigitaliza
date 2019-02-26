
nombre = str(input('Nombre: '))
apellidos = str(input('Apellidos: '))
ciudad = str(input('Ciudad: '))
edad = str(input('Edad: '))
telefono = str(input('Telefono: '))

if nombre == "" or apellidos == "" or edad == "" or ciudad == "" or telefono == "":
    print('Datos incorrectos')
else:
    if type(edad) == int:
        print('Mi nombre es '+nombre+' '+apellidos+'. Tengo '+str(edad)+' años y vivo en '+ciudad+'.\nSi quieren contactar conmigo llamen a '+telefono)
    else:
        print('Edad incorrecta')

