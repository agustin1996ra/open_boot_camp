import time


def main():
    hora = time.localtime().tm_hour
    if 8 < hora < 19:
        print(f'Te quedan {19 - hora} de trabajo.')
    else:
        print('Es hora de ir a casa.')


if __name__ == '__main__':
    main()
