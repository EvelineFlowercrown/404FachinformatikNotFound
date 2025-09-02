#BezugsPreisRechner

listenEinkaufsPreis = int(input("listenPreis in €: "))
rabatt = int(input("rabatt in %: "))
sconto = int(input("sconto in %: "))
bezugsKosten = int(input("bezugsKosten in €: "))
mwst = int(input("Mehrwertsteuer in %: "))

zielEinkaufsPreis = round(listenEinkaufsPreis*(1-(rabatt/100)),2)
barEinkaufsPreis = round(zielEinkaufsPreis*(1-(sconto/100)),2)

if mwst == 0:
    if sconto == 0:
        print("ZieleinkaufsPreis:", zielEinkaufsPreis, "€")
        print("Zahlbetrag:", zielEinkaufsPreis+bezugsKosten, "€")
    else:
        print("Bareinkaufspreis:", barEinkaufsPreis, "€")
        print("Zahlbetrag:", barEinkaufsPreis+bezugsKosten, "€")
else:
    if sconto == 0:
        print("ZieleinkaufsPreis:",zielEinkaufsPreis,"€","inkl.",mwst,"% MwSt.:",round(zielEinkaufsPreis*(1+(mwst/100)),2))
        print("Zahlbetrag:",zielEinkaufsPreis+bezugsKosten,"€","inkl.",mwst,"% MwSt.:",round(zielEinkaufsPreis*(1+(mwst/100)),2)+bezugsKosten)
    else:
        print("Bareinkaufspreis:",barEinkaufsPreis,"€","inkl.",mwst,"% MwSt.:",round(barEinkaufsPreis*(1+(mwst/100)),2))
        print("Zahlbetrag:",barEinkaufsPreis+bezugsKosten,"€","inkl.",mwst,"% MwSt.:",round(barEinkaufsPreis*(1+(mwst/100)),2)+bezugsKosten)
