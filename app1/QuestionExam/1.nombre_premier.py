def est_premier(nombre_a_tester):
    if nombre_a_tester < 2:
        return False
    for i in range(2, int(nombre_a_tester ** 0.5) + 1):
        if nombre_a_tester % i == 0:
            return False
    return True

def tester_nombre():
    nombre_a_tester = int(input("Entrez un nombre : "))
    if est_premier(nombre_a_tester):
        print(f"{nombre_a_tester} est un nombre premier.")
    else:
        print(f"{nombre_a_tester} n'est pas un nombre premier.")


if __name__ == '__main__':
    tester_nombre()