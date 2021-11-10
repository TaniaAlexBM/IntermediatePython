# función principal
def run():
    myList = [1, 'Hello', True, 4.5]
    myDict = {'firstname': 'Facundo', 'lastname':'García'}

    superList = [
        {'firstname': 'Facundo', 'lastname':'García'},
        {'firstname': 'Miguel', 'lastname':'Torres'},
        {'firstname': 'Pepe', 'lastname':'Rodelo'},
        {'firstname': 'Susana', 'lastname':'Martínez'},
        {'firstname': 'José', 'lastname':'García'}
    ]

    superDict = {
        'naturalNums': [1,2,3,4,5],
        'integgerNums':[-1,-2,0,1,2],
        'floatingNums':[1.1,4.5,6.43]
    }

    for key,value in superDict.items():
        print(key, '-', value)

    for i in range(len(superList)):
        j = superList[i]
        for key,value in j.items():
            print(key,'-',value)

    for i in range(1,101):
        print(i**2)

# enterpoint
if __name__ == '__main__':
    run()