def produit(*args):
    total = 1
    for valeur in args:
        total *= valeur
    return total

print(produit(1, 2))
print(produit(1, 2, 3, 4))