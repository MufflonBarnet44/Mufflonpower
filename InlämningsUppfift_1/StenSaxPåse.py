stenimport random

def avgör_vinnare(spelare, dator):
    if spelare == dator:
        return "oavgjort"
    elif (spelare == "sten" and dator == "sax") or \
         (spelare == "sax" and dator == "påse") or \
         (spelare == "påse" and dator == "sten"):
        return "vinst"
    else:
        return "förlust"

valmöjligheter = ["sten", "sax", "påse"]

print("Välkommen till Sten-Sax-Påse!")
while True:
    spelare_val = input("Välj sten, sax eller påse: ").strip().lower()
    if spelare_val not in valmöjligheter:
        print("Ogiltigt val, försök igen.")
        continue

    dator_val = random.choice(valmöjligheter)
    print(f"Du valde: {spelare_val}")
    print(f"Datorn valde: {dator_val}")

    resultat = avgör_vinnare(spelare_val, dator_val)

    if resultat == "oavgjort":
        print("Det blev oavgjort! Försök igen.\n")
    else:
        print(f"Du {resultat}!")
        break
