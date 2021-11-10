def read():
    numbers = []
    # Para que compile todos los caracteres, se utiliza encoding
    with open('./archivos/numbers.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Facundo','Miguel','Pepe','Christian','Rocío']
    with open('./archivos/names.txt', 'a', encoding='UTF-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    write()

if __name__ == '__main__':
    run()