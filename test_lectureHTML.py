def lecture(fichier_HTML): 
    with open (fichier_HTML, "r") as f: 
        text = f.read()
    return text 

c = lecture("document_bf_1.html")
print(c)