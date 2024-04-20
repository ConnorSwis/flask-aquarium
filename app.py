from flask import Flask, jsonify, render_template
import random
import threading
import time

app = Flask(__name__)


class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.position = {'x': random.random(), 'y': random.random()}
        self.last_position_x = self.position['x']

    def move(self):
        self.last_position_x = self.position['x']
        r = 0.05
        dx = random.uniform(-r, r)
        dy = random.uniform(-r, r)
        self.position['x'] = max(0.1, min(self.position['x'] + dx, 0.9))
        self.position['y'] = max(0.2, min(self.position['y'] + dy, 0.75))


class Aquarium:
    def __init__(self):
        self.fishes = [Fish('Bubbles', 'Goldfish'), Fish('Flash', 'Betta')]

    def status(self):
        return [{'name': fish.name, 'species': fish.species, 'position': fish.position, 'last_position_x': fish.last_position_x} for fish in self.fishes]

    def update(self):
        while True:
            for fish in self.fishes:
                fish.move()
            time.sleep(3)


aquarium = Aquarium()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(aquarium.status())


def run_aquarium_updates():
    aquarium.update()


updater_thread = threading.Thread(target=run_aquarium_updates, daemon=True)
updater_thread.start()
