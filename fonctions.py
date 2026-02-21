def saluer():
    print("Bonjour depuis une fonction !")
saluer() 
print("Ravi de te voir")
saluer()
def bonjour(prenom):
    print(f"Salut {prenom} !")
saluer()
bonjour("Alice")
bonjour("Mohamed")
def presentation(nom, age):
    print(f"Je m'apelle {nom} et j'ai {age} ans.")
    presentation("Alice", 30)