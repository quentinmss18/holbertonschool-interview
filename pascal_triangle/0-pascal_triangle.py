def pascal_triangle(n):
    """
    Retourne une liste de listes d'entiers représentant le triangle de Pascal de n.
    """
    if n <= 0:
        return []

    # Initialisation avec la première ligne
    triangle = [[1]]

    # On boucle de 1 à n-1 pour créer les lignes suivantes
    for i in range(1, n):
        prev_row = triangle[-1]  # La ligne précédente
        # La nouvelle ligne commence toujours par 1
        current_row = [1]
        
        # On calcule les éléments entre les deux extrémités
        for j in range(1, i):
            # Somme des deux éléments au-dessus
            val = prev_row[j - 1] + prev_row[j]
            current_row.append(val)
        
        # La nouvelle ligne se termine toujours par 1
        current_row.append(1)
        
        # On ajoute la ligne terminée au triangle
        triangle.append(current_row)

    return triangle
