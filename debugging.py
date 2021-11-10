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
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Terminó mi programa')
    except ValueError:
        print('Debes ingresar un número')

if __name__ == '__main__':
    run()