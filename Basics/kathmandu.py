from random import choice

capital="Mahrajgunj"
bird="danphe"
flower="Sunflower"
song="Kutu ma kutu"

def randomfunfact():
    funfact= [
        "Kathmandu is big city",
        "There are many people there.",
        "It is the hub of trade",
        "A very touristy place"
    ]

    index = choice("0123")
    print(funfact[int(index)])

if __name__ == "__main__":
    randomfunfact()