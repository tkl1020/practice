import tkinter as tk
import math
import time

# Basic setup
WIDTH = 800
HEIGHT = 400
AMPLITUDE = 100
FREQUENCY = 0.05
SPEED = 0.1

class SineWaveApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.phase = 0
        self.line = None
        self.animate()

    def animate(self):
        self.canvas.delete("wave")
        points = []
        for x in range(WIDTH):
            y = HEIGHT // 2 + AMPLITUDE * math.sin(FREQUENCY * x + self.phase)
            points.append(x)
            points.append(y)
        self.canvas.create_line(points, fill='lime', tags="wave", smooth=True, width=2)
        self.phase += SPEED
        self.canvas.after(16, self.animate)  # ~60 FPS

# Run it
root = tk.Tk()
root.title("Wibblin' and Wobblin' Sin Wave")
app = SineWaveApp(root)
root.mainloop()
