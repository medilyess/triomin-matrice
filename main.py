import numpy as np

def affiche(M):
    """for i in range(x):
        for j in range(y):
            print(M[i,j], end="\t")
        print("\n")"""
    print(M.view())

def remplir(M):
    for i in range(x):
        for j in range(y):
            if M[i, j] != -1:
                M[i, j] = 1

def blackPointPos(M, a, b):
    if a <= x/2-1 and b <= y/2-1:
        return "Top left"
    elif a >= x/2 and b <= y/2-1:
        return "Top right"
    elif a <= x/2-1 and b >= y/2:
        return "Bottom left"
    elif a >= x/2 and b >= y/2:
        return "Bottom right"



if __name__ == "__main__":
    n = int(input("Donner la taille du matrice: "))
    M = np.zeros((n, n), int)
    x, y = M.shape
    L = list(map(int, input("Donner la position du trou noir: ").split()))
    a, b = L[0], L[1]
    M[a, b] = -1
    #ch = blackPointPos(M, a, b)
    remplir(M)
    #print(x/2-1, x/2, y/2-1, y/2)
    affiche(M)
    """match ch:
        case "Top left":"""
