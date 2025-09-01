# ============================================
# Python Übungsblatt – Grundlagen Fortgeschritten
# ============================================
# Lektion 3: Kleine Projekte und komplexere Aufgaben
# ============================================

# 1. Dictionaries
# Lege ein Dictionary mit 3 Schülernamen als Schlüssel an
# und den jeweiligen Noten als Werte.
# Gib alle Namen und Noten schön formatiert aus.

noten = {"Eveline":4, "Lennart":2, "TJ":1}
for key in noten.keys():
    print(f"{key} - {noten[key]}")

# 2. Wörter zählen in einem Text
# Lass den Benutzer einen Satz eingeben.
# Zähle, wie oft jedes Wort vorkommt.
# Tipp: Dictionary verwenden.

beispieltext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
wortZähler = {}
for wort in beispieltext.split(" "):
    if wort in wortZähler:
        wortZähler[wort]+=1
    else: wortZähler.update({wort:1})
#nicht für aufgabe nötig - sortiert die dictionary einträge anhand ihrer values
for key, value in sorted(wortZähler.items(), key=lambda item: item[1], reverse=True):
    print(f"{key} - {value}")

# 3. Funktionen & Wiederverwendung
# Schreibe eine Funktion, die eine Liste von Zahlen als Parameter bekommt
# und das Minimum, Maximum und den Durchschnitt zurückgibt.
# Teste die Funktion mit einer eigenen Liste.

def analyzeIntList(intList):
    min =  2**31 - 1
    max = -2**31 + 1
    sum = 0
    for int in intList:
        sum += int
        min = int*(int<min) + min*(min<int)
        max = int * (int > max) + max * (max > int)
    return (min,max,sum/len(intList))

myInts = [0,12,634,21,2,-9]
print(analyzeIntList(myInts))

# 4. Dateiverarbeitung (neu!)
# Schreibe ein Programm, das eine Textdatei einliest (z.B. "daten.txt").
# Gib den gesamten Inhalt aus.
# Zähle, wie viele Zeilen die Datei hat.
# Tipps:
# with open("pfad","r/w/rw",encoding="utf-8"
# readlines()
# ../ um vom aktuellen file aus nach oben in der ordnerstruktur zu navigieren.

with open("../LiesMichAus.txt", "r", encoding="utf-8") as file:
    print(file.readlines())
    print(f"Die Datei hat {len(file.readlines())} Zeilen")

# 5. Verschachtelte Schleifen
# Erstelle ein kleines 1x1-Programm:
# Gib die Multiplikationstabelle von 1 bis 10 als Tabelle aus.

for i in range(1,11):
    zeile = []
    for j in range(1,11):
        zeile.append(i*j)
    print(zeile)

# 6. Einfaches Hangman-Spiel
# - Lege ein geheimes Wort fest (z.B. "python").
# - Der Benutzer rät Buchstaben.
# - Wenn der Buchstabe enthalten ist, wird er im Wort aufgedeckt,
#   sonst gibt es einen Fehlerpunkt.
# - Nach 8 Fehlern hat der Spieler verloren, ansonsten gewonnen.

word = "python"
fehler = 0
guessedChars = []
while fehler < 8:
    obfuscated = ""
    for char in word:
        if char not in guessedChars:
            obfuscated += "_ "
        else: obfuscated += f"{char} "
    if "_" not in obfuscated:
        print(obfuscated)
        print("gewonnen")
        break
    print(obfuscated)
    guess = input("rate einen buchstaben \n")
    if guess not in word:
        fehler+=1
    else: guessedChars.append(guess)

# 7. Bonus – Taschenrechner
# Schreibe ein kleines Programm, das wiederholt:
#   - eine Zahl
#   - eine Rechenoperation (+, -, *, /)
#   - eine zweite Zahl
# vom Benutzer einliest.
# Gib das Ergebnis aus und wiederhole, bis der Benutzer "ende" eingibt.

while True:
    n1 = input("number 1: ")
    if n1 == "stop":
        break
    n1 = int(n1)
    op = input("operator: ")
    n2 = int(input("number 2: "))
    result = 0

    match op:
        case "+":
            result = n1+n2
        case "-":
            result = n1-n2
        case "*":
            result = n1*n2
        case "/":
            result = n1/n2
    print(result)
