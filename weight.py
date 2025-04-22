
try:
        weight = float(input("Enter you weight: "))
except ValueError:
        print("Invalid input, use number stupid")
        error = True

        if not error:
            unit = input("Kilograms or Pounds (P or K)")

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

