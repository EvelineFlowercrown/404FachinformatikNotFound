import pandas as pd
import matplotlib.pyplot as plt

#Beurteilung
beispielBeurteilung = {
    "Anschaffungskosten":(25,2500,2000),
    "Bedienungskomfort":(30,1,6),
    "Füllmenge":(20,4,6),
    "Wasserverbrauch":(10,80,40),
    "Stromverbrauch":(15,2500,1500)
}

beispielKandidaten = {
    "Miele":{
        "Anschaffungskosten":2500,
        "Bedienungskomfort":6,
        "Füllmenge":5,
        "Wasserverbrauch":50,
        "Stromverbrauch":2000},
    "Bosch":{
        "Anschaffungskosten":2300,
        "Bedienungskomfort":5,
        "Füllmenge":6,
        "Wasserverbrauch":60,
        "Stromverbrauch":2200},
    "Gastro":{
        "Anschaffungskosten":2200,
        "Bedienungskomfort":4,
        "Füllmenge":5,
        "Wasserverbrauch":55,
        "Stromverbrauch":2000}
}

def clamp(value,min,max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

def inputBeurteilung():
    print("input stop to exit")
    gesamtGewichtung = 0
    beurteilung = {}
    while True:
        kategorie = input("Beurteilungskategorie hinzufügen:")
        if kategorie == "stop" and gesamtGewichtung == 100:
            break
        elif gesamtGewichtung > 100:
            raise Exception
        gewichtung = int(input("gewichtung:"))
        noPoints = int(input("Null Punkte Wert:"))
        fullPoints = int(input("Zehn Punkte Wert:"))
        gesamtGewichtung += gewichtung
        beurteilung.update({kategorie:(gewichtung,noPoints,fullPoints)})
    return beurteilung

def inputCandidate(beurteilung):
    Kandidaten = {}
    while True:
        print("input stop to exit")
        name = input("Beurteilungskategorie hinzufügen:")
        if name == "stop":
            break
        werte = {}
        for kategorie in beurteilung.keys():
            wert = int(input(f"{kategorie}:"))
            werte.update({kategorie:wert})
        Kandidaten.update({name:werte})
    return Kandidaten

def nutzwertAnalyse(Kandidaten, bewertung):
    kandidatenTabelle = {"kategorie/Kandidat":Kandidaten.keys()}
    #Kategorien einfügen
    for kategorie in bewertung.keys():
        kandidatenTabelle.update({kategorie:[]})
        gewichtung, noPoints, fullPoints = bewertung[kategorie]
        for kandidat in Kandidaten.keys():
            wert = Kandidaten[kandidat][kategorie]
            punkte = clamp(((wert-noPoints)/((fullPoints-noPoints)/10))*(gewichtung/10),0,gewichtung)
            kandidatenTabelle[kategorie].append(f"{wert} - {punkte}/{gewichtung}")
    df = pd.DataFrame(kandidatenTabelle)
    renderTable(df)

def renderTable(dataFrame):
    # Als Bild rendern
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis('off')

    # Tabelle zeichnen
    tabelle = ax.table(
        cellText=dataFrame.values,
        colLabels=dataFrame.columns,
        loc='center',
        cellLoc='center'
    )

    # Tabellen-Style anpassen
    tabelle.auto_set_font_size(False)
    tabelle.set_fontsize(9)
    tabelle.scale(1.2, 1.2)

    plt.savefig("nutzwertanalyse.png", dpi=300, bbox_inches="tight")
    plt.show()





nutzwertAnalyse(beispielKandidaten, beispielBeurteilung)