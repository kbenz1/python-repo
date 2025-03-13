# Datei schreiben
with open("meine_daten.txt","w") as datei:
    datei.write("Python ist großartig!")

# Datei lesen
with open("meine_daten.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)
