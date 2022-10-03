import calculadora as calc


def main():
    a = 5
    b = 13
    print('a =', a)
    print('b =', b)
    print(f'a + b = {calc.sumar(a, b)}')
    print(f'a - b = {calc.restar(a, b)}')
    print(f'a * b = {calc.multiplicar(a, b)}')
    print(f'a / b = {calc.dividir(a, b)}')


if __name__ == '__main__':
    main()
