def accum(word):
    return "-".join(c.upper() + c.lower() * i for i, c in enumerate(word))

print(accum("AsdzsdsaA"))



