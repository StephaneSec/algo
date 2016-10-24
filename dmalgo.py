def arbrebinomial(A, n, p, decal=2):
    """
    Donne le code LaTeX/TikZ pour un le trace d'un arbre de probabilite
    correspondant a une loi binomiale.
    La variable A est une chaine de caracteres, par exemple : A = "A"
    Le parametre 'decal' est optionnel et vaut 2 par defaut.
    """
    texte = "\\begin{tikzpicture}[xscale=1,yscale=1]\n"
    q = 1 - p
    evenement = "$\overline{{{}}}$".format(A)
    contraire = "${}$".format(A)
    for h in range(n):
        for v in range(2**(n-h)):
            if h == 0:
                ajoutv = 0
            else:
                ajoutv = 0.5*sum(2**i for i in range(h))
            if v % 2 == 0:
                v = ajoutv + v*2**h
                x0, y0, x1, y1 = -h*decal, v, -h*decal-decal, v+0.5*2**h
                texte += "\\draw ({},{})--({},{}) ".format(x0, y0, x1, y1)
                texte += "node[midway, below, sloped]{{{}}};\n".format(q)
            else:
                v = ajoutv + v*2**h
                x0, y0, x1, y1 = -h*decal, v, -h*decal-decal, v-0.5*2**h
                texte += "\\draw ({},{})--({},{}) ".format(x0, y0, x1, y1)
                texte += "node[midway, above, sloped]{{{}}};\n".format(p)
    for h in range(n):
        for v in range(2**(n-h)):
            if h ==0:
                ajoutv = 0
            else:
                ajoutv = 0.5*sum(2**i for i in range(h))
            if v % 2 == 0:
                v = ajoutv + v*2**h
                x, y = -h*decal, v
                texte += "\\draw ({},{}) ".format(x, y)
                texte += "node[fill=white]{{{}}};\n".format(evenement)
            else:
                v = ajoutv + v*2**h
                x, y = -h*decal, v
                texte += "\\draw ({},{}) ".format(x, y)
                texte += "node[fill=white]{{{}}};\n".format(contraire)
    texte += "\\end{tikzpicture}"
    return texte
print(arbrebinomial(``A'',3,0.4))

