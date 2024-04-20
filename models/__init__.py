import random
import time


X_MIN, X_MAX = 0.1, 0.9
Y_MIN, Y_MAX = 0.1, 0.9
MAX_VELOCITY = 0.03

fish_names = [
    "Fin Diesel", "Gillbert", "Swim Shady", "Bubba Gump", "Fish and Chips", "Captain Jack Sparrowfin",
    "James Pond", "H2Oprah", "Kanye West Coast", "Salmongela Merkel", "Trout Bader Ginsburg",
    "Cod Stewart", "Gill Clinton", "Algae Baldwin", "Clammy Fallon", "Scarlet Johansson",
    "Krillem Dafoe", "Mackerelmore", "Anchovy Hopkins", "Betta White", "Salmon Cowell",
    "Guppy Goldberg", "Flounder Woods", "Aquaman", "Barracuda Obama", "Codzilla",
    "Finn Affleck", "Sharkira", "Meryl Streepfin"
]

class Fish:
    def __init__(self, name, species_index):
        self.name = name
        self.species = f"Species {species_index + 1}"
        self.image = f"fish{species_index + 1}.png"
        self.position = {'x': random.uniform(X_MIN, X_MAX), 'y': random.uniform(Y_MIN, Y_MAX)}
        self.velocity = {'dx': random.uniform(-MAX_VELOCITY, MAX_VELOCITY), 'dy': random.uniform(-MAX_VELOCITY, MAX_VELOCITY)}

    def move(self):
        bound_position = lambda pos, min_val, max_val: max(min_val, min(pos, max_val))
        update_vel = lambda v, dc: bound_position(v + (dc if random.random() >= 0.1 else 0), -MAX_VELOCITY, MAX_VELOCITY)

        self.position['x'] = bound_position(self.position['x'] + self.velocity['dx'], X_MIN, X_MAX)
        self.position['y'] = bound_position(self.position['y'] + self.velocity['dy'], Y_MIN, Y_MAX)

        self.velocity['dx'] = update_vel(self.velocity['dx'], random.uniform(-0.01, 0.01))
        self.velocity['dy'] = update_vel(self.velocity['dy'], random.uniform(-0.01, 0.01))

        if self.position['x'] == X_MIN or self.position['x'] == X_MAX:
            self.velocity['dx'] = -self.velocity['dx']
        if self.position['y'] == Y_MIN or self.position['y'] == Y_MAX:
            self.velocity['dy'] = -self.velocity['dy']


class Aquarium:
    def __init__(self):
        self.fishes = [Fish(random.choice(fish_names), i % 8) for i in range(8)]

    def status(self):
        return [{
            'name': fish.name,
            'species': fish.species,
            'position': fish.position,
            'velocity': fish.velocity,
            'image': fish.image
        } for fish in self.fishes]

    def update(self):
        while True:
            for fish in self.fishes:
                fish.move()
            time.sleep(6)