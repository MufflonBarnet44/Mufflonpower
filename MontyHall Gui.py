import tkinter as tk
import random

class MontyHallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Monty Hall-spelet")
        self.reset_game()

        self.info_label = tk.Label(root, text="Välj en dörr", font=("Arial", 14))
        self.info_label.pack(pady=10)

        # Skapa canvas för att rita dörrarna
        self.canvas = tk.Canvas(root, width=600, height=200)
        self.canvas.pack(pady=10)

        # Dörrknappar (representeras som rektanglar)
        self.door_width = 100
        self.door_height = 150
        self.buttons = []
        for i in range(3):
            btn = self.canvas.create_rectangle(150 + i * 150, 50, 150 + i * 150 + self.door_width, 50 + self.door_height, fill="gray")
            self.canvas.tag_bind(btn, "<Button-1>", lambda event, i=i: self.select_door(i))
            self.buttons.append(btn)

        self.stats_label = tk.Label(root, text="", font=("Arial", 12))
        self.stats_label.pack(pady=10)

    def reset_game(self):
        self.car_door = random.randint(0, 2)
        self.selected_door = None
        self.revealed_door = None
        self.switch_wins = 0
        self.stay_wins = 0
        self.total_switch = 0
        self.total_stay = 0
        self.game_in_progress = True

    def select_door(self, choice):
        if not self.game_in_progress:
            return

        self.selected_door = choice

        # Välj en dörr att avslöja som inte är spelarens val eller bilen
        possible_doors = [i for i in range(3) if i != self.selected_door and i != self.car_door]
        self.revealed_door = random.choice(possible_doors)

        # Visa den valda dörren
        self.canvas.itemconfig(self.buttons[self.selected_door], fill="blue")

        # Visa den avslöjade dörren
        self.canvas.itemconfig(self.buttons[self.revealed_door], fill="white")
        self.canvas.create_text(150 + self.revealed_door * 150 + self.door_width / 2, 50 + self.door_height / 2, text="Nitlott", fill="black", font=("Arial", 10))

        # Ändra texten
        self.info_label.config(text="Vill du byta dörr?")

        self.create_choice_buttons()
        self.game_in_progress = False

    def create_choice_buttons(self):
        self.switch_button = tk.Button(self.root, text="Byt dörr", command=self.switch_choice)
        self.switch_button.pack(pady=5)
        self.stay_button = tk.Button(self.root, text="Stanna kvar", command=self.stay_choice)
        self.stay_button.pack(pady=5)

    def end_game(self, won, switched):
        # Visa resultat
        for btn in self.buttons:
            self.canvas.itemconfig(btn, fill="white")  # Alla dörrar avslöjas

        # Visa om bilen var bakom den valda dörren
        if self.selected_door == self.car_door:
            self.canvas.itemconfig(self.buttons[self.selected_door], fill="red")
            self.canvas.create_text(150 + self.selected_door * 150 + self.door_width / 2, 50 + self.door_height / 2, text="BIL", fill="white", font=("Arial", 10))
        else:
            self.canvas.itemconfig(self.buttons[self.selected_door], fill="gray")

        result = "Vinst!" if won else "Förlust"
        self.info_label.config(text=f"{result} Bilen var bakom dörr {self.car_door+1}.")

        # Uppdatera statistik
        if switched:
            self.total_switch += 1
            if won:
                self.switch_wins += 1
        else:
            self.total_stay += 1
            if won:
                self.stay_wins += 1

        # Visa statistik
        stats_text = (
            f"Bytt dörr: {self.switch_wins}/{self.total_switch} vinster\n"
            f"Stannat kvar: {self.stay_wins}/{self.total_stay} vinster"
        )
        self.stats_label.config(text=stats_text)

        # Knapp för att spela igen
        self.play_again_button = tk.Button(self.root, text="Spela igen", command=self.new_game)
        self.play_again_button.pack(pady=10)

    def switch_choice(self):
        # Byt till dörren som inte valdes eller avslöjades
        final_choice = [i for i in range(3) if i != self.selected_door and i != self.revealed_door][0]
        won = final_choice == self.car_door
        self.end_game(won, switched=True)

        self.switch_button.destroy()
        self.stay_button.destroy()

    def stay_choice(self):
        won = self.selected_door == self.car_door
        self.end_game(won, switched=False)

        self.switch_button.destroy()
        self.stay_button.destroy()

    def new_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

# Kör spelet
if __name__ == "__main__":
    root = tk.Tk()
    app = MontyHallGame(root)
    root.mainloop()


