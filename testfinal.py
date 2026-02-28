import os

#Vérifie si la liste est vide.
def est_vide(P):
    return P == []
#Ajoute un élément e au sommet de la pile.
def empiler(P, e):
    P.append(e)
    return P
#Retire l'élément au sommet.
def depiler(P):
    if not est_vide(P):
        P.pop()
    return P
#Regarde l'élément au sommet sans le retirer.
def sommet(P):
    if est_vide(P):
        return None
    return P[-1]
#Ajoute un élément à la fin de la file.
def enfiler(F, e):
    F.append(e)
    return F
#Retire et renvoie le premier élément de la file.
def defiler(F):
    if not est_vide(F):
        return F.pop(0)
    return None

#Cette fonction parcourt la chaîne de caractères (le code HTML) pour en extraire uniquement les noms des balises.
def analyser_html(html_brut):
    file_balises = []
    i = 0
    solo_balise = ['img', 'br', 'hr', 'input', 'meta', 'link']
    
    while i < len(html_brut):
        if html_brut[i] == "<":
            fin = html_brut.find(">", i)
            if fin != -1:
                contenu = html_brut[i+1:fin].split()[0].replace("/", "")
                est_fermante = html_brut[i+1] == "/"
                
                if contenu.lower() not in solo_balise:
                    nom = "/" + contenu if est_fermante else contenu
                    enfiler(file_balises, nom)
                i = fin
        i += 1
    return file_balises

# --- 3. RAPPORT D'ERREURS (Étapes 2 & 3 de la mission) ---
#Elle utilise une pile de contrôle pour vérifier la symétrie du document.
def verifier_structure(file_balises):
    pile_controle = []
    rapport_erreurs = []

    # On traite chaque balise dans l'ordre de la file
    while len(file_balises) > 0:
        b = defiler(file_balises)
        
        if not b.startswith("/"):
            # Balise ouvrante -> on empile
            empiler(pile_controle, b)
        else:
            # Balise fermante -> on vérifie le sommet
            nom_pur = b[1:]
            if est_vide(pile_controle):
                rapport_erreurs.append(f"Erreur : Balise fermante </{nom_pur}> sans ouverture.")
            elif sommet(pile_controle) == nom_pur:
                # Match parfait, on dépile le sommet
                depiler(pile_controle)
            else:
                rapport_erreurs.append(f"Erreur : Trouvé </{nom_pur}>, mais attendait </{sommet(pile_controle)}>.")
                depiler(pile_controle)

    # Vérification des balises jamais fermées
    while not est_vide(pile_controle):
        rapport_erreurs.append(f"Erreur : Balise <{sommet(pile_controle)}> non fermée en fin de document.")
        depiler(pile_controle)

    return rapport_erreurs


# --- 4. EXÉCUTION ---

def lecture(fichier_HTML): 
    with open(fichier_HTML, "r") as f: 
        text = f.read()
    return text 

if __name__ == "__main__":
    nom_fichier = input("Entrez le nom du fichier HTML: ")

    if os.path.exists(nom_fichier): 
        c = lecture(nom_fichier)
        print("Analyse du code en cours...")
        
        file_a_traiter = analyser_html(c)
        erreurs = verifier_structure(file_a_traiter)
        
        # On affiche le rapport
        print("\n--- RAPPORT FINAL ---")
        if not erreurs:
            print("Félicitations : Aucune erreur de structure détectée !")
        else:
            for index, err in enumerate(erreurs, 1):
                print(f"{index}. {err}")
    else: 
        print("Désolé le fichier n'existe pas")