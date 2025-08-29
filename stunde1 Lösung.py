# ============================================
# Python Übungsblatt – Grundlagen
# ============================================
# Aufgabe: Ergänze den fehlenden Code unter jedem Kommentar.
# Ziel: Erste Schritte in Python verstehen und anwenden.
# ============================================


# 1. Ausgabe auf der Konsole
# Schreibe ein Programm, das "Hallo Welt" auf dem Bildschirm ausgibt.

print("Hallo Welt")

# 2. Variablen
# Lege eine Variable 'name' an und speichere darin deinen Namen.
# Gib dann die Variable mit print() aus.

name = "Eveline"

# 3. Rechnen mit Zahlen
# Lege zwei Variablen 'a' und 'b' an (z.B. 5 und 3).
# Berechne die Summe, die Differenz, das Produkt und den Quotienten.
# Gib die Ergebnisse aus.

a = 5
b= 3

diff = a-b
sum = a+b
prod = a*b
quot = a/b

print(diff)
print(sum)
print(prod)
print(quot)

# 4. Benutzereingaben
# Lass den Benutzer eine Zahl eingeben (input()).
# Wandle die Eingabe in einen Integer um und gib das Doppelte dieser Zahl aus.

zahlAlsString = input("gib eine Zahl ein")
doppelteZahlAlsInt = int(zahlAlsString)*2
# python ist recht schlau und kann datentypen selbstständig umwandeln
# daher würde auch print(zahlAlsString*2) reichen
print(doppelteZahlAlsInt)

# 5. Bedingungen (if/else)
# Schreibe ein Programm, das prüft, ob eine eingegebene Zahl gerade oder ungerade ist.
# Tipp: Nutze den Modulo-Operator (%).

zahl = input("gib eine Zahl ein")
if zahl % 2 == 1:
    print("zahl ist ungerade")
else:
    print("zahl ist gerade")

# 6. Schleifen – for
# Schreibe eine Schleife, die die Zahlen von 1 bis 10 ausgibt.

for i in range(1,10):
    print(i)

# 7. Schleifen – while
# Schreibe eine Schleife, die so lange läuft, bis der Benutzer "stop" eingibt.

userInput = "" #leerer string
while userInput != "stop":
    userInput = input("wenn du stop eingibst stoppt das programm")

# 8. Listen
# Lege eine Liste mit drei Früchten an (z.B. ["Apfel", "Banane", "Kirsche"]).
# Gib die ganze Liste und danach jedes Element einzeln in einer Schleife aus.

liste = ["Apfel", "Banane", "Kirsche"]
print(liste)
for element in liste:
    print(element)

# 9. Funktionen
# Schreibe eine Funktion, die zwei Zahlen als Parameter nimmt
# und deren Summe zurückgibt.
# Teste die Funktion mit zwei Beispielen.

def addiereZweiZahlen(zahl1, zahl2):
    return zahl1+zahl2

# 10. Bonus: Wörter zählen
# Schreibe ein Programm, das einen Satz vom Benutzer einliest
# und dann die Anzahl der Wörter im Satz ausgibt.
# Tipp: split()

beispieltext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
anzahlWörter = 0
split = beispieltext.split(" ")
print(len(split))
print(split)
