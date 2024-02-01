varfrase =input("Escriba una frase")
varletra = input("Escriba una letra")
varcontar = 0
varl =0
while varl < len(varfrase):
    if varfrase[varl].lower() == varletra.lower():
        varcontar += 1
    varl +=1
print(f"La letra {varletra} se encuentra {varcontar} veces en la frase escrita")