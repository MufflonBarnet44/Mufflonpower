import random
import matplotlib.pyplot as plt

def monty_hall_simulation(num_trials):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        car_position = random.randint(0, 2)
        player_choice = 0
        possible_doors = [i for i in range(3) if i != player_choice and i != car_position]
        door_opened_by_host = random.choice(possible_doors)
        remaining_door = [i for i in range(3) if i != player_choice and i != door_opened_by_host][0]

        if player_choice == car_position:
            stay_wins += 1
        if remaining_door == car_position:
            switch_wins += 1

    return stay_wins, switch_wins

# Kör simuleringen
num_trials = 100000
stay_wins, switch_wins = monty_hall_simulation(num_trials)

# Beräkna vinstprocent
stay_win_percentage = (stay_wins / num_trials) * 100
switch_win_percentage = (switch_wins / num_trials) * 100

# Skriv ut vinstprocent i terminalen
print(f"Vinstprocent – Stanna kvar: {stay_win_percentage:.1f}%, Byta: {switch_win_percentage:.1f}%")

# Rita stapeldiagram med procent
labels = ['Stanna kvar', 'Byta']
wins = [stay_wins, switch_wins]
percentages = [stay_win_percentage, switch_win_percentage]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, wins, color=['blue', 'green'])
plt.title(f'Monty Hall-simulering ({num_trials} spel)')
plt.ylabel('Antal vinster')

# Lägg till procentsatser ovanför staplarna
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 10, f'{percentage:.1f}%', 
             ha='center', va='bottom', fontsize=12)

plt.ylim(0, max(wins) + 100)
plt.show()
