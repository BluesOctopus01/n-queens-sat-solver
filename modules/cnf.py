def variable(i: int, j: int, n: int) -> int:
    """
    Associe un identifiant SAT unique à la variable x_ij.

    i : numéro de ligne
    j : numéro de colonne
    n : taille de l'échiquier

    Les indices commencent à 1.
    L'identifiant est compris entre 1 et n2.
    """
    return (i - 1) * n + j


def contraintes_ligne(n: int, clauses: list[list[int]]) -> None:
    """
    Impose au maximum une reine par ligne.

    Pour chaque case (i, j), si une reine est présente,
    alors aucune autre case (i, l), avec l != j,
    ne peut contenir une reine.

    Contrainte : x_ij -> -x_il, avec l != j.
    Forme CNF : -x_ij V -x_il
    """

    # Parcourir toutes les cases (i, j) de l'échiquier
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Parcourir les autres colonnes l de la même ligne i
            for l in range(1, n + 1):
                # Exclure la case de départ (l != j)
                if l != j:
                    # Convertir les coordonnées en identifiants SAT
                    x1 = variable(i, j, n)
                    x2 = variable(i, l, n)
                    # les deux cases ne peuvent pas être occupées simultanément
                    clauses.append([-x1, -x2])


def contraintes_colonne(n: int, clauses: list[list[int]]) -> None:
    """
    Impose au maximum une reine par colonne.

    Pour chaque case (i, j), si une reine est présente,
    alors aucune autre case (k, j), avec k != i,
    ne peut contenir une reine.

    Contrainte : x_ij -> -x_kj, avec k != i
    Forme CNF : -x_ij V -x_kj
    """

    # Parcourir toutes les cases (i, j) de l'échiquier
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Parcourir les autres lignes k de la même colonne j
            for k in range(1, n + 1):
                # Exclure la case de départ (k != i)
                if k != i:
                    # Convertir les coordonnées en identifiants SAT
                    x1 = variable(i, j, n)
                    x2 = variable(k, j, n)
                    # les deux cases ne peuvent pas être occupées simultanément
                    clauses.append([-x1, -x2])


def contraintes_diagonale_desc(n: int, clauses: list[list[int]]) -> None:
    """
    Impose au maximum une reine par diagonale descendante.

    Pour chaque case (i, j), si une reine est présente,
    alors aucune autre case (k, l) située sur la même
    diagonale descendante ne peut contenir une reine.

    Sur une diagonale descendante :
        j - i = l - k
        donc l = j + k - i

    Contrainte : x_ij -> -x_kl, avec k != i et 1 <= l <= n.
    Forme CNF : -x_ij V -x_kl.
    """
    # Parcourir toutes les cases (i, j) de l'échiquier
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Parcourir les lignes k pour chercher les cases
            # appartenant à la même diagonale descendante
            for k in range(1, n + 1):
                # Ne pas comparer la case avec elle-même
                if k != i:
                    # Calculer la colonne sur la même diagonale : j - i = l - k
                    l = j + k - i
                    # Vérifier que la colonne l existe dans le tableau
                    if 1 <= l <= n:
                        # Convertir les coordonnées en identifiants SAT
                        x1 = variable(i, j, n)
                        x2 = variable(k, l, n)
                        # Interdire deux reines simultanément
                        # sur les cases (i, j) et (k, l)
                        clauses.append([-x1, -x2])


def contraintes_diagonale_mont(n: int, clauses: list[list[int]]) -> None:
    """
    Impose au maximum une reine par diagonale montante.

    Pour chaque case (i, j), si une reine est présente,
    alors aucune autre case (k, l) située sur la même
    diagonale montante ne peut contenir une reine.

    Sur une diagonale montante :
        j + i = l + k
        donc l = j + i - k

    Contrainte : x_ij -> -x_kl, avec k != i et 1 <= l <= n.
    Forme CNF : -x_ij V -x_kl.
    """
    # Parcourir toutes les cases (i, j) de l'échiquier
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Parcourir les lignes k pour chercher les cases
            # appartenant à la même diagonale montante
            for k in range(1, n + 1):
                # Ne pas comparer la case avec elle-même
                if k != i:
                    # Calculer la colonne sur la même diagonale : j + i = l + k
                    l = j + i - k
                    # Vérifier que la colonne l existe dans le tableau
                    if 1 <= l <= n:
                        # Convertir les coordonnées en identifiants SAT
                        x1 = variable(i, j, n)
                        x2 = variable(k, l, n)
                        # Interdire deux reines simultanément
                        # sur les cases (i, j) et (k, l)
                        clauses.append([-x1, -x2])


def contraintes_existence(n: int, clauses: list[list[int]]) -> None:
    """
    Impose au moins une reine par ligne.

    Pour chaque ligne i, au moins une des cases (i, j)
    doit contenir une reine.

    Contrainte : x_i1 V x_i2 V ... V x_in
    Forme CNF : ∧(1 à n) [x_i1 V x_i2 V ... V x_in]
    """

    for i in range(1, n + 1):
        # Créer une nouvelle clause pour chaque ligne
        clause = []

        # Parcourir chaque colonne j de la ligne i
        for j in range(1, n + 1):
            # Convertir les coordonnées en identifiant SAT
            x = variable(i, j, n)
            clause.append(x)

        # Ajouter la clause d'existence de la ligne
        clauses.append(clause)


def generer_cnf(n: int) -> list[list[int]]:
    """
    Génère la formule CNF du problème des N reines.

    Regroupe les contraintes de lignes, colonnes,
    diagonales descendantes, diagonales montantes
    et d'existence d'au moins une reine par ligne.

    Retourne une liste de clauses CNF, chaque clause
    étant représentée par une liste d'entiers SAT.
    """
    clauses = []

    contraintes_ligne(n, clauses)
    contraintes_colonne(n, clauses)
    contraintes_diagonale_desc(n, clauses)
    contraintes_diagonale_mont(n, clauses)
    contraintes_existence(n, clauses)

    return clauses
