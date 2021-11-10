def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num%i == 0:
            divisors.append(i)
    try:
        if num < 0:
            raise ValueError('Ingresa un número positivo')
        return divisors
    except ValueError as NegativeError:
        print(NegativeError)

def run():
        num = input('Ingresa un número: ')
        assert num.isnumeric(), 'Debes ingresar un número'
        print(divisors(int(num)))
        print('Terminó mi programa')

if __name__ == '__main__':
    run()