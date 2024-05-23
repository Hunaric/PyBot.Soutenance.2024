
def replace_values_with_keys(text):
    # Charger le dictionnaire depuis le fichier
    with open("read.txt", 'r', encoding='utf-8') as file:
        dictionary = eval(file.read())  # Attention : utilisez eval uniquement si vous avez confiance dans la source du fichier

    for key, value in dictionary.items():
        if value in text:
            text = text.replace(value, key)
    return text

# Exemple de variable response
response = "Voici quelques quartiers : Wologuede, Gbedjromede et Akpakpa."

response = replace_values_with_keys(response)

# Afficher le résultat
print(response)
