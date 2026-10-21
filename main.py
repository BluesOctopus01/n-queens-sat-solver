from modules.cnf import generer_cnf
from modules.interface import askN, afficherSolutions, afficherClauses
from modules.sat_solver import resoudre


def main() -> None:
    """
    Point d'entrée du programme des N reines.

    Demande la taille de l'échiquier, génère les contraintes
    CNF, recherche toutes les solutions avec le solveur SAT
    et affiche les résultats dans la console.
    """

    # 1. Demander la taille de l'échiquier
    n = askN()

    # 2. Générer et afficher les informations sur la CNF
    clauses = generer_cnf(n)
    afficherClauses(clauses)

    # 3. Résoudre le problème avec PySAT
    solutions = resoudre(clauses, n)

    # 4. Afficher les solutions trouvées
    afficherSolutions(solutions, n)


if __name__ == "__main__":
    main()
