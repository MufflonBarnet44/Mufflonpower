
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Skapa graf
plt.plot(x, y)
plt.title("Enkel linjegraf")
plt.xlabel("x-axel")
plt.ylabel("y-axel")
plt.grid(True)

# Visa grafen
plt.show()

