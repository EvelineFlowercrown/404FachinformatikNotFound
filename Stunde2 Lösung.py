# ============================================
# Python Übungsblatt – Grundlagen Vertiefung
# ============================================
# Lektion 2: Das Gelernte anwenden und kombinieren
# ============================================
import math
import random

# 1. Rechnen & Bedingungen
# Schreibe ein Programm, das zwei Zahlen vom Benutzer einliest.
# Gib aus, welche Zahl größer ist oder ob beide gleich groß sind.

a = input("zahl 1:")
b = input("zahl 2:")
print(a*(a>b)+b*(b>a))

# 2. Schleifen & Bedingungen
# Gehe mit einer Schleife über alle Zahlen von 1 bis 50 aus.
# gib die Zahlen nur mit print() aus wenn sie ein Vielfaches von 3, oder ein Vielfaches von 5 ist.
# Tipp: if/elif/else

for i in range(1,51):
    if i % 5 == 0 or i % 3 == 0:
        print(i)

# 3. Listen verarbeiten
# Lege eine Liste mit beliebigen 5 Zahlen an.
# Gib die größte Zahl aus.
# Berechne außerdem die Summe aller Zahlen in der Liste.

def getRandomIntList():
    list = []
    for i in range(0,5):
        rand = random.randint(0, 100)
        list.append(rand)
    return list


list = getRandomIntList()
highestValue = 0
for element in list:
    if element>highestValue:
        highestValue = element
print(highestValue)

# 4. Listen & Benutzereingabe
# Frage den Benutzer wiederholt nach einem Wort.
# Beende die Eingabe, wenn der Benutzer "stop" schreibt.
# Speichere alle Wörter in einer Liste und gib sie am Ende aus.

wordList = []
lastInput = ""
while lastInput != "stop":
    lastInput = input("schreibe stop um zu stoppen")
    wordList.append(lastInput)
print(wordList)

# 5. Funktionen wiederholen
# Schreibe eine Funktion, die prüft, ob eine Zahl eine Primzahl ist.
# (Primzahl = nur durch 1 und sich selbst teilbar)
# Teste die Funktion mit mehreren Zahlen.

def isPrime(zahl):
    for i in range(2,int(math.sqrt(zahl))):
        if zahl % i == 0 and i != zahl:
            return False
    return True

# 6. Kombination: Zahlenraten-Spiel
# - Wähle eine Zufallszahl zwischen 1 und 100 (Tipp: import random).
# - Der Benutzer soll raten, welche Zahl es ist.
# - Nach jedem Tipp soll das Programm sagen, ob die Zahl größer oder kleiner ist.
# - Beende das Spiel, wenn die Zahl erraten wurde.

zahl = random.randint(1,101)
while True:
    try: geraten = int(input("Errate die zahl!"))
    except: geraten = 0
    if zahl > geraten: print("gues higher")
    elif zahl < geraten: print("gues lower")
    else: break

# 7. Bonus – Text-Statistik
# Lass den Benutzer einen längeren Text eingeben.
# Zähle:
#   - wie viele Wörter vorkommen
#   - wie viele Zeichen der Text hat
#   - wie oft der Buchstabe "e" vorkommt
# Gib die Ergebnisse aus.

beispieltext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
anzahlWörter = len(beispieltext.split(" "))
anzahlZeichen = len(beispieltext)
anzahlE = len(beispieltext.split("e"))
print(f"Anzahl Wörter = {anzahlWörter}, Anzahl Zeichen = {anzahlZeichen}, Anzahl 'e' = {anzahlE}")

