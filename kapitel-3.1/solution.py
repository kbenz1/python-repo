import csv

# Datei schreiben
with open("produkte.csv", "w", newline="") as datei:
    writer = csv.writer(datei)
    writer.writerow(["Produkt", "Preis", "Menge"])
    writer.writerow(["Apfel", 0.50, 10])
    writer.writerow(["Banane", 0.30, 20])
    writer.writerow(["Orange", 0.80, 15])

# Datei lesen
with open("produkte.csv", "r") as datei:
    reader = csv.reader(datei)
    for zeile in reader:
        print(zeile)
