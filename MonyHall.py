import random
import matplotlib.pyplot as plt

# Simulera Monty Hall-problemet
def monty_hall_simulation(num_trials):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        # Placera bil bakom en av dörrarna
        car_position = random.randint(0, 2)
        
        # Spelaren väljer en dörr (alltid dörr 0)
        player_choice = 0
        
        # Spelledaren öppnar en dörr som inte har bilen och inte är spelarens val
        possible_doors = [i for i in range(3) if i != player_choice and i != car_position]
        door_opened_by_host = random.choice(possible_doors)
        
        # Den dörr som är kvar att byta till
        remaining_door = [i for i in range(3) if i != player_choice and i != door_opened_by_host][0]
        
        # Om man stannar
        if player_choice == car_position:
            stay_wins += 1
        
        # Om man byter
        if remaining_door == car_position:
            switch_wins += 1

    return stay_wins, switch_wins

# Kör simuleringen
num_trials = 1000
stay_wins, switch_wins = monty_hall_simulation(num_trials)

# Visualisera resultatet
labels = ['Stanna kvar', 'Byta']
wins = [stay_wins, switch_wins]

plt.figure(figsize=(8, 5))
plt.bar(labels, wins, color=['blue', 'green'])
plt.title(f'Monty Hall-simulering ({num_trials} spel)')
plt.ylabel('Antal vinster')
plt.show()
