def lecture(fichier_HTML): 
    with open (fichier_HTML, "r") as f: 
        text = f.read()
    return text 

nom_fichier = input("Entrez le nom du fichier HTML: ")

if os.path.exists(nom_ficher): 
    c = lecture(nom_fichier)
    print(c) 
else: 
    print("Désoler le fichier n'existe pas") 
