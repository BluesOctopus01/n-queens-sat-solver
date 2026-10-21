from pysat.solvers import Glucose3


def resoudre(clauses: list[list[int]], n: int) -> list[list[int]]:
    """
    Recherche toutes les solutions du problème des N reines
    à partir des contraintes CNF générées.

    Utilise le solveur SAT Glucose3 pour énumérer toutes
    les affectations qui satisfont les contraintes.

    Pour chaque modèle SAT, conserve uniquement les
    identifiants positifs correspondant aux cases
    contenant une reine.

    Retourne une liste de solutions, chaque solution
    étant une liste d'identifiants SAT.
    """
    solutions = []

    # Initialiser le solveur avec les contraintes CNF
    with Glucose3(bootstrap_with=clauses) as solveur:
        # Parcourir tous les modèles satisfaisant les contraintes
        for modele in solveur.enum_models():
            reines = []

            # Examiner les variables du modèle SAT
            for x in modele:
                # Conserver uniquement les variables vraies
                # représentant les cases de l'échiquier
                if 1 <= x <= n * n:
                    reines.append(x)

            # Ajouter la configuration trouvée aux solutions
            solutions.append(reines)

    return solutions
