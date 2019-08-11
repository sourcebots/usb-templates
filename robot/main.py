import time
from sbot import Note, Robot

r = Robot()

# Play a tune
tune = [
    Note.C6,
    Note.E6,
    Note.G6,
    Note.C7,
]
for note in tune:
    r.power_board.piezo.buzz(0.5, note)
    time.sleep(0.5)
