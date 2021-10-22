import random
import re


def generaPassword(lunghezza):
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    speciali = ("@!#$%'-/=^\_`{}~+'")
    numeri = ('0123456789')
    gruppo = caratteri + speciali + numeri
    while True:
        password = ''
        for i in range(0, int(lunghezza)):
            password += random.choice(gruppo)
        if validaPassword(password):
            break
        else:
            print('{}: non mi piace , la rifaccio ..'.format(password))
    return password


def validaPassword(password):
    isOk = ('^.*(?=.{'+str(len(password))+',})(?=.*\d)(?=.*[a-z])'
                         '(?=.*[A-Z])(?=.*[!£$%&#=?]).*$')
    return re.findall(isOk, password)


if __name__ == '__main__':
    lunghezza = input('lunghezza password -> ')
    passGenerata = generaPassword(lunghezza)
    print()
    print('Ecco la tua password: {}'.format(passGenerata))