from math import sqrt

def main():
    DL = {i:i**3 for i in range(1,101) if i%3 != 0}
    print(DL)

    # RETO
    reto = {i:sqrt(i) for i in range(1,1001)}
    print(reto)

if __name__ == '__main__':
    main()