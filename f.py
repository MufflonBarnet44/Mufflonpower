error = False  # Definiera en boolesk variabel för att hålla koll på om ett fel inträffade

try:
    weight = float(input("Enter your weight: "))  # Försök att konvertera inmatningen till ett flyttal
except ValueError:  # Om en ValueError inträffar (om användaren inte matar in ett nummer)
    print("Invalid input, use number stupid")
    error = True  # Sätt error till True om ett fel inträffar

# Om inget fel inträffade (error == False), fortsätt att fråga om enhet
if not error:  # Om error är False (inget fel inträffade)
    unit = input("Kilograms or Pounds (P or K): ")  # Fråga om enhet
    if unit == "K" : 
                weight = weight * 2.205
                unit = "Lbs."
                print(f"Your weight is : {round(weight, 1)} {unit}")
    elif unit == "L" : 
                 weight = weight / 2.205
                 unit = "Kg."
                 print(f"Your weight is : {round(weight, 1)} {unit}")  
    else: 
                 print(f"{unit} was not valid")

else:
    print("Please enter a valid weight next time.")