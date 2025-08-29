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
    wortZähler.update()

# 3. Funktionen & Wiederverwendung
# Schreibe eine Funktion, die eine Liste von Zahlen als Parameter bekommt
# und das Minimum, Maximum und den Durchschnitt zurückgibt.
# Teste die Funktion mit einer eigenen Liste.


# 4. Dateiverarbeitung (neu!)
# Schreibe ein Programm, das eine Textdatei einliest (z.B. "daten.txt").
# Gib den gesamten Inhalt aus.
# Zähle, wie viele Zeilen die Datei hat.
# (Tipp: open(), read(), readlines())


# 5. Verschachtelte Schleifen
# Erstelle ein kleines 1x1-Programm:
# Gib die Multiplikationstabelle von 1 bis 10 als Tabelle aus.


# 6. Einfaches Hangman-Spiel
# - Lege ein geheimes Wort fest (z.B. "python").
# - Der Benutzer rät Buchstaben.
# - Wenn der Buchstabe enthalten ist, wird er im Wort aufgedeckt,
#   sonst gibt es einen Fehlerpunkt.
# - Nach 8 Fehlern hat der Spieler verloren, ansonsten gewonnen.


# 7. Bonus – Taschenrechner
# Schreibe ein kleines Programm, das wiederholt:
#   - eine Zahl
#   - eine Rechenoperation (+, -, *, /)
#   - eine zweite Zahl
# vom Benutzer einliest.
# Gib das Ergebnis aus und wiederhole, bis der Benutzer "ende" eingibt.
