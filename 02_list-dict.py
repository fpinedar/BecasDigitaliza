def printList(nombre,list):
    print('Imprimiendo Lista de',nombre)
    for element in list:
        print(element, end=" ")
    print('\n')


print('Sentencias Listas')
list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_string = ['cerezo', 'pino', 'manzano', 'roble', 'alcornoque']
list_mixed = ['noche', 4, 5.0, 'dia', 6.0, 4]

print(list_integer)
print(list_string)
print(list_mixed)
print()

printList('Enteros',list_integer)
printList('Strings',list_string)
printList('Mixed',list_mixed)

last_list_integer=list_integer[-1]
last_list_string=list_string[-1]
last_list_mixed=list_mixed[-1]

print('Ultimos valores => (Integer: '+str(last_list_integer)+'); (String: '+str(last_list_string)+'); (Mixed: '+str(last_list_mixed)+');\n')

print('Sentencias Diccionarios')
dict_films = {'Avatar':'James Cameron','Matrix':'Wachowski','Star Wars':'George Lucas'}
print(dict_films)
print(dict_films.keys())
print(dict_films.values())