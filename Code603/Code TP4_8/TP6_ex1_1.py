#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      utilisateur
#
# Created:     09/02/2024
# Copyright:   (c) utilisateur 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Particle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Gestion des collisions avec les bords du conteneur
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.speed_y = -self.speed_y

# Paramètres du conteneur
width, height = 10, 10

# Création de particules
num_particles = 10
particles = [Particle(random.uniform(1, width-1), random.uniform(1, height-1), 0.2) for _ in range(num_particles)]

# Fonction d'initialisation de l'animation
def init():
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    return []

# Fonction appelée à chaque trame de l'animation
def update(frame):
    ax.clear()

    for particle in particles:
        particle.move()
        ax.add_patch(plt.Circle((particle.x, particle.y), particle.radius, color='red'))

    return []

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Animation
animation = FuncAnimation(fig, update, init_func=init, frames=200, blit=True, interval=50)
plt.show()
