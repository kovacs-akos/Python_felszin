import math


def felszin_szamitas():
    print('===========================')
    print('Testek felszín számítása:')
    adott_input = input('Írj egy "K"-t a kockáért, "T"-t a téglatestért. Írj egy "0"-t, ha ki szeretnél lépni a programból: ').capitalize()
    felszin: int = 0
    if adott_input == "K":
        kocka_el = int(input('Add meg a kocka élét cm-ben: '))
        felszin = 6 * kocka_el * kocka_el
        print(f'A négyzet felszíne: {felszin}cm2')
    elif adott_input == "T":
        elso_el = int(input('Add meg a téglatest első élét cm-ben: '))
        masodik_el = int(input('Add meg a téglatest második élét cm-ben: '))
        harmadik_el = int(input('Add meg a téglatest élét harmadik cm-ben: '))
        felszin = 2 * (elso_el * masodik_el + elso_el * harmadik_el + masodik_el * harmadik_el)
        print(f'A téglatest felszíne: {felszin}cm2')
    elif adott_input == "0":
        print('Program leállítása...')
        quit()
    else:
        print('Az általad megadott opció nem létezik!')
    print('============================')


def main() -> None:
    felszin_szamitas()
    while True:
        valasztas = int(input('A program újboli lefuttatásához írj egy "1"-est: '))
        if valasztas == 1:
            felszin_szamitas()
        else:
            print('Program leállítása...')
            quit()


if __name__ == "__main__":
    main()
