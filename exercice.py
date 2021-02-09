#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []
    for prefixe in prefixes:
        noms.append(prefixe + suffixe)

    return noms


def prime_integer_summation() -> int:
    #24133
    nombre = 1
    nb_premier = []
    somme = 0
    while len(nb_premier) < 100:
        nombre += 1
        nb_premier.append(nombre)
        for i in range(2, nombre):
            if nombre % i == 0:
                nb_premier.remove(nombre)
                break
    for nb in nb_premier:
        somme += nb
    return somme


def factorial(number: int) -> int:
    factorielle = 1
    for nombre in range(1, number + 1):
        factorielle *= nombre
    return factorielle


def use_continue() -> None:
    for nombre in range(1, 11):
        if nombre == 5:
            continue
        else:
            print(nombre)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    validite = []
    for groupe in groups:
        if 3 < len(groupe) < 10:
            for age in groupe:
                if age == 25:
                    validite.append(True)
                    break
                elif age < 18:
                    validite.append(False)
                    break
                elif age < 70 and age == 50:
                    validite.append(False)
                    break
                else:
                    validite.append(True)
                    break
        else:
            validite.append(False)



    return validite


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
