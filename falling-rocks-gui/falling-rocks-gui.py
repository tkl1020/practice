import tkinter as tk
import random
import time
import pygame

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 20
ROCK_WIDTH = 40
ROCK_HEIGHT = 20
ROCK_SPAWN_INTERVAL = 1000  # ms
ROCK_SPEED = 4
PLAYER_SPEED = 6

class Rock:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, WINDOW_WIDTH - ROCK_WIDTH)
        self.y = -ROCK_HEIGHT
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + ROCK_WIDTH, self.y + ROCK_HEIGHT, fill="gray")

    def move(self):
        self.y += ROCK_SPEED
        self.canvas.coords(self.shape, self.x, self.y, self.x + ROCK_WIDTH, self.y + ROCK_HEIGHT)

    def is_off_screen(self):
        return self.y > WINDOW_HEIGHT

class FallingRocksGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Smooth Falling Rocks")

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.high_scores = []
        self.start_game()

        self.root.bind("<KeyPress-Left>", self.go_left)
        self.root.bind("<KeyPress-Right>", self.go_right)
        self.root.bind("<KeyRelease-Left>", self.stop)
        self.root.bind("<KeyRelease-Right>", self.stop)

        pygame.mixer.init()
        pygame.mixer.music.load("fzero_midi.wav")  # MIDI-style wav file
        pygame.mixer.music.play(-1)  # loop forever

    def start_game(self):
        self.player_x = WINDOW_WIDTH / 2
        self.player_y = WINDOW_HEIGHT - 40
        self.player_shape = self.canvas.create_rectangle(
            self.player_x - PLAYER_WIDTH / 2, self.player_y,
            self.player_x + PLAYER_WIDTH / 2, self.player_y + PLAYER_HEIGHT,
            fill="white"
        )
        self.rocks = []
        self.move_direction = 0
        self.game_over = False
        self.last_spawn = time.time()
        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", text=f"Score: {self.score}", fill="white", font=("Courier", 14))
        self.update_game()

    def go_left(self, event):
        self.move_direction = -1

    def go_right(self, event):
        self.move_direction = 1

    def stop(self, event):
        self.move_direction = 0

    def spawn_rock(self):
        self.rocks.append(Rock(self.canvas))

    def update_game(self):
        if self.game_over:
            return

        # Move player
        self.player_x += self.move_direction * PLAYER_SPEED
        self.player_x = max(0 + PLAYER_WIDTH / 2, min(WINDOW_WIDTH - PLAYER_WIDTH / 2, self.player_x))

        self.canvas.coords(
            self.player_shape,
            self.player_x - PLAYER_WIDTH / 2, self.player_y,
            self.player_x + PLAYER_WIDTH / 2, self.player_y + PLAYER_HEIGHT
        )

        # Move rocks
        for rock in self.rocks:
            rock.move()

        # Remove off-screen rocks and update score
        new_rocks = []
        for rock in self.rocks:
            if rock.is_off_screen():
                self.score += 1
            else:
                new_rocks.append(rock)
        self.rocks = new_rocks
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

        # Collision detection
        for rock in self.rocks:
            if (rock.y + ROCK_HEIGHT > self.player_y and
                rock.y < self.player_y + PLAYER_HEIGHT and
                rock.x < self.player_x + PLAYER_WIDTH / 2 and
                rock.x + ROCK_WIDTH > self.player_x - PLAYER_WIDTH / 2):
                self.end_game()
                return

        # Spawn new rocks
        if time.time() - self.last_spawn > ROCK_SPAWN_INTERVAL / 1000:
            self.spawn_rock()
            self.last_spawn = time.time()

        self.root.after(16, self.update_game)  # ~60 FPS

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2 - 30,
            text="💀 GAME OVER 💀",
            fill="red",
            font=("Courier", 28)
        )
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2 + 10,
            text=f"Final Score: {self.score}\nEnter your name:",
            fill="white",
            font=("Courier", 14)
        )
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.name_entry.focus()
        self.name_entry.bind("<Return>", self.save_high_score)

    def save_high_score(self, event):
        name = self.name_entry.get()
        self.high_scores.append((name, self.score))
        self.high_scores.sort(key=lambda x: x[1], reverse=True)
        self.name_entry.destroy()
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2 + 60,
            text="Press Enter to Restart",
            fill="yellow",
            font=("Courier", 14)
        )
        self.root.bind("<Return>", self.restart_game)

    def restart_game(self, event):
        self.canvas.delete("all")
        self.root.unbind("<Return>")
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = FallingRocksGame(root)
    root.mainloop()

