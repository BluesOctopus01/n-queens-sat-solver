from modules.cnf import variable


def askN() -> int:
    """
    Présente le programme et demande la taille de l'échiquier.
    Vérifie que l'utilisateur saisit un entier positif.
    """

    print("=" * 50)
    print("           RÉSOLVEUR DES N REINES")
    print("=" * 50)
    print("Résolution par logique propositionnelle (CNF/SAT).")
    print("Le programme recherche toutes les configurations")
    print("valides de N reines sur un échiquier N x N.")
    print("=" * 50)

    n = 0

    while n < 1:
        try:
            n = int(input("\nTaille de l'échiquier (N >= 1) : "))

            if n < 1:
                print("Erreur : veuillez entrer un entier positif.")

        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

    return n


def afficherClauses(clauses: list[list[int]]) -> None:
    print(f"\nNombre de clauses CNF : {len(clauses)}")


def afficherEchiquier(solution: list[int], n: int):
    """
    Affiche un échiquier dans la console.

    Q représente une reine.
    . représente une case vide.
    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            case = variable(i, j, n)

            if case in solution:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


def afficherSolutions(solutions, n):
    """
    Permet de parcourir les solutions dans le terminal.

    Entrée : solution suivante.
    p : solution précédente.
    q : quitter la consultation.
    """

    if not solutions:
        print(f"Pas de solution pour un échiquier {n}x{n}")
        return
    numero = 0

    while numero < len(solutions):
        print(f"\nSolution {numero + 1} / {len(solutions)}\n")
        afficherEchiquier(solutions[numero], n)

        choix = input("\n[Entrée] Suivante | [p] Précédente | [q] Quitter : ")

        if choix == "q":
            print("\nFin de la consultation des solutions.")
            return

        elif choix == "p" and numero > 0:
            numero -= 1

        elif choix == "":
            numero += 1
