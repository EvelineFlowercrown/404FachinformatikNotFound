# ============================================
# Python Übungsblatt – Grundlagen Fortgeschritten
# ============================================
# Lektion 3: Kleine Projekte und komplexere Aufgaben
# ============================================


# 1. Dictionaries
# Lege ein Dictionary mit 3 Schülernamen als Schlüssel an
# und den jeweiligen Noten als Werte.
# Gib alle Namen und Noten schön formatiert aus.
# 👉 Dictionaries speichern Paare: dict = {schlüssel: wert}



# 2. Wörter zählen in einem Text
# Lass den Benutzer einen Satz eingeben.
# Zähle, wie oft jedes Wort vorkommt.
# Tipp: Dictionary verwenden.
# 👉 dict.get(key, 0) liefert einen Wert oder 0, wenn der Schlüssel nicht existiert.



# 3. Funktionen & Wiederverwendung
# Schreibe eine Funktion, die eine Liste von Zahlen als Parameter bekommt
# und das Minimum, Maximum und den Durchschnitt zurückgibt.
# Teste die Funktion mit einer eigenen Liste.
# 👉 min(liste), max(liste) geben kleinste/größte Zahl zurück.
# 👉 sum(liste)/len(liste) berechnet den Durchschnitt.



# 4. Dateiverarbeitung (neu!)
# Schreibe ein Programm, das eine Textdatei einliest (z.B. "daten.txt").
# Gib den gesamten Inhalt aus.
# Zähle, wie viele Zeilen die Datei hat.
# Tipps:
# with open("pfad","r/w/rw",encoding="utf-8":
# readlines()
# ../ um vom aktuellen file aus nach oben in der ordnerstruktur zu navigieren.
# 👉 with open("datei.txt", "r") as f: öffnet eine Datei.
# 👉 f.read() liest alles.
# 👉 f.readlines() liefert eine Liste der Zeilen.



# 5. Verschachtelte Schleifen
# Erstelle ein kleines 1x1-Programm:
# Gib die Multiplikationstabelle von 1 bis 10 als Tabelle aus.
# 👉 Verschachtelte for-Schleifen erlauben Tabellenstrukturen.



# 6. Einfaches Hangman-Spiel
# - Lege ein geheimes Wort fest (z.B. "python").
# - Der Benutzer rät Buchstaben.
# - Wenn der Buchstabe enthalten ist, wird er im Wort aufgedeckt,
#   sonst gibt es einen Fehlerpunkt.
# - Nach 8 Fehlern hat der Spieler verloren, ansonsten gewonnen.
# 👉 "a" in "abc" prüft, ob "a" enthalten ist.



# 7. Bonus – Taschenrechner
# Schreibe ein kleines Programm, das wiederholt:
#   - eine Zahl
#   - eine Rechenoperation (+, -, *, /)
#   - eine zweite Zahl
# vom Benutzer einliest.
# Gib das Ergebnis aus und wiederhole, bis der Benutzer "ende" eingibt.
# 👉 while True: erlaubt eine Endlosschleife (mit break beenden).