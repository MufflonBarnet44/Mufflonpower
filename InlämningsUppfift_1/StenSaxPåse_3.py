import tkinter as tk
import random
import time

# Poäng
spelare_poäng = 0
dator_poäng = 0

# Val
val = ["sten", "sax", "påse"]

# Avgör vinnare
def avgör_vinnare(spelare, dator):
    if spelare == dator:
        return "oavgjort"
    elif (spelare == "sten" and dator == "sax") or \
         (spelare == "sax" and dator == "påse") or \
         (spelare == "påse" and dator == "sten"):
        return "vinst"
    else:
        return "förlust"

# Animation
def visa_animation(spelare, dator, resultat):
    animation_label.config(text="")  # Nollställ

    if resultat == "oavgjort":
        animation_label.config(text="Båda valde samma – det blev oavgjort!")
        return

    if spelare == "sax" and dator == "påse":
        text = "✂️ Saxen klipper sönder påsen!"
    elif spelare == "påse" and dator == "sten":
        text = "🧻 Påsen fångar stenen!"
    elif spelare == "sten" and dator == "sax":
        text = "🪨 Stenen krossar saxen!"
    elif dator == "sax" and spelare == "påse":
        text = "✂️ Datorns sax klipper din påse!"
    elif dator == "påse" and spelare == "sten":
        text = "🧻 Datorns påse fångar din sten!"
    elif dator == "sten" and spelare == "sax":
        text = "🪨 Datorns sten krossar din sax!"
    else:
        text = ""

    animation_label.config(text="")
    for i in range(len(text) + 1):
        animation_label.config(text=text[:i])
        root.update()
        time.sleep(0.05)  # Liten "skriv-effekt"

# Spela ett drag
def spela(spelar_val):
    global spelare_poäng, dator_poäng

    dator_val = random.choice(val)
    resultat = avgör_vinnare(spelar_val, dator_val)

    if resultat == "vinst":
        spelare_poäng += 1
    elif resultat == "förlust":
        dator_poäng += 1

    resultat_text.set(
        f"Du valde: {spelar_val}\n"
        f"Datorn valde: {dator_val}\n"
        f"Resultat: {resultat}\n\n"
        f"Ställning: Du {spelare_poäng} - {dator_poäng} Datorn"
    )

    visa_animation(spelar_val, dator_val, resultat)

    if spelare_poäng == 2 or dator_poäng == 2:
        if spelare_poäng > dator_poäng:
            slutresultat = "🎉 Du vann bäst av 3!"
        else:
            slutresultat = "😔 Datorn vann bäst av 3!"
        resultat_text.set(resultat_text.get() + f"\n\n{slutresultat}")
        inaktivera_spel()

# Stoppa spelet
def inaktivera_spel():
    sten_knapp.config(state="disabled")
    sax_knapp.config(state="disabled")
    påse_knapp.config(state="disabled")
    nytt_spel_knapp.pack(pady=5)
    avsluta_knapp.pack(pady=5)

# Nytt spel
def nytt_spel():
    global spelare_poäng, dator_poäng
    spelare_poäng = 0
    dator_poäng = 0
    resultat_text.set("Välj sten, sax eller påse:")
    animation_label.config(text="")
    sten_knapp.config(state="normal")
    sax_knapp.config(state="normal")
    påse_knapp.config(state="normal")
    nytt_spel_knapp.pack_forget()
    avsluta_knapp.pack_forget()

# GUI
root = tk.Tk()
root.title("Sten-Sax-Påse – Bäst av 3")

resultat_text = tk.StringVar()
resultat_text.set("Välj sten, sax eller påse:")
resultat_label = tk.Label(root, textvariable=resultat_text, font=("Arial", 14), pady=10, justify="left")
resultat_label.pack()

# Animation-text
animation_label = tk.Label(root, text="", font=("Arial", 16), fg="darkred", pady=10)
animation_label.pack()

# Val-knappar
sten_knapp = tk.Button(root, text="🪨 Sten", width=15, command=lambda: spela("sten"))
sax_knapp = tk.Button(root, text="✂️ Sax", width=15, command=lambda: spela("sax"))
påse_knapp = tk.Button(root, text="🧻 Påse", width=15, command=lambda: spela("påse"))

sten_knapp.pack(pady=5)
sax_knapp.pack(pady=5)
påse_knapp.pack(pady=5)

# Nytt spel / Avsluta
nytt_spel_knapp = tk.Button(root, text="🔁 Nytt spel", width=15, command=nytt_spel)
avsluta_knapp = tk.Button(root, text="🚪 Avsluta", width=15, command=root.quit)

root.mainloop()
