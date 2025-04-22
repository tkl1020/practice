import tkinter as tk
from tkinter import filedialog
from PIL import Image
import random
import math

PALETTE = [
    "#000000", "#FFFFFF", "#FF0000", "#00FF00",
    "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF",
    "#808080", "#800000", "#808000", "#008000",
    "#800080", "#008080", "#000080", "#C0C0C0"
]

class PixelEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Editor")

        self.grid_size = 32
        self.cell_size = 16
        self.color = PALETTE[0]
        self.pixels = []
        self.pixel_data = []
        self.sprite_style = tk.StringVar(value="Random")

        self.create_menu()
        self.create_canvas()
        self.create_palette()
        self.create_controls()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        size_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Grid Size", menu=size_menu)
        for size in [16, 32, 64]:
            size_menu.add_command(label=f"{size} x {size}", command=lambda s=size: self.resize_grid(s))

        menubar.add_command(label="Save as PNG", command=self.save_image)

    def create_canvas(self):
        if hasattr(self, 'canvas_frame'):
            self.canvas_frame.destroy()

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.grid(row=0, column=0, rowspan=2)

        canvas_width = self.grid_size * self.cell_size
        canvas_height = self.grid_size * self.cell_size

        self.canvas = tk.Canvas(self.canvas_frame, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

        self.draw_grid()

    def draw_grid(self):
        self.pixels = []
        self.pixel_data = []
        self.canvas.delete("all")

        for y in range(self.grid_size):
            row = []
            data_row = []
            for x in range(self.grid_size):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
                row.append(rect)
                data_row.append("#FFFFFF")
            self.pixels.append(row)
            self.pixel_data.append(data_row)

    def paint(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            self.canvas.itemconfig(self.pixels[y][x], fill=self.color)
            self.pixel_data[y][x] = self.color

    def create_palette(self):
        palette_frame = tk.Frame(self.root)
        palette_frame.grid(row=0, column=1, sticky="nw", padx=10)

        tk.Label(palette_frame, text="Color Palette").pack()
        for color in PALETTE:
            btn = tk.Button(palette_frame, bg=color, width=2, height=1,
                            command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=1, pady=1)

    def create_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.grid(row=1, column=1, sticky="sw", padx=10)

        clear_btn = tk.Button(control_frame, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=5)

        sprite_styles = ["Random", "Symmetrical", "Monochrome", "Geometric Pattern", "AI Pattern"]
        style_menu = tk.OptionMenu(control_frame, self.sprite_style, *sprite_styles)
        style_menu.pack(side=tk.LEFT, padx=5)

        random_btn = tk.Button(control_frame, text="Generate Sprite", command=self.generate_random_sprite)
        random_btn.pack(side=tk.LEFT, padx=5)

    def set_color(self, color):
        self.color = color

    def clear_canvas(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.canvas.itemconfig(self.pixels[y][x], fill="white")
                self.pixel_data[y][x] = "#FFFFFF"

    def resize_grid(self, new_size):
        self.grid_size = new_size
        self.create_canvas()

    def generate_random_sprite(self):
        style = self.sprite_style.get()

        if style == "Random":
            for y in range(self.grid_size):
                for x in range(self.grid_size):
                    color = random.choice(PALETTE)
                    self.canvas.itemconfig(self.pixels[y][x], fill=color)
                    self.pixel_data[y][x] = color

        elif style == "Monochrome":
            main_color = random.choice(PALETTE)
            for y in range(self.grid_size):
                for x in range(self.grid_size):
                    color = main_color if random.random() > 0.5 else "#FFFFFF"
                    self.canvas.itemconfig(self.pixels[y][x], fill=color)
                    self.pixel_data[y][x] = color

        elif style == "Symmetrical":
            for y in range(self.grid_size):
                half = self.grid_size // 2
                row_colors = [random.choice(PALETTE) for _ in range(half)]
                full_row = row_colors + row_colors[::-1]
                for x in range(self.grid_size):
                    color = full_row[x]
                    self.canvas.itemconfig(self.pixels[y][x], fill=color)
                    self.pixel_data[y][x] = color

        elif style == "Geometric Pattern":
            center = self.grid_size // 2
            for y in range(self.grid_size):
                for x in range(self.grid_size):
                    dx = abs(x - center)
                    dy = abs(y - center)
                    distance = int((dx ** 2 + dy ** 2) ** 0.5)
                    color = PALETTE[distance % len(PALETTE)]
                    self.canvas.itemconfig(self.pixels[y][x], fill=color)
                    self.pixel_data[y][x] = color

        elif style == "AI Pattern":
            center = self.grid_size // 2
            symmetry = random.choice([True, False])
            base_colors = random.sample(PALETTE, k=4)

            for y in range(self.grid_size):
                for x in range(self.grid_size // 2):
                    angle = math.atan2(y - center, x - center)
                    wave = math.sin(angle * 5 + random.random())
                    color_index = int((abs(wave) * len(base_colors)) % len(base_colors))
                    color = base_colors[color_index]

                    self.canvas.itemconfig(self.pixels[y][x], fill=color)
                    self.pixel_data[y][x] = color

                    if symmetry:
                        mirror_x = self.grid_size - x - 1
                        self.canvas.itemconfig(self.pixels[y][mirror_x], fill=color)
                        self.pixel_data[y][mirror_x] = color

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        img = Image.new("RGB", (self.grid_size, self.grid_size), "white")
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = self.pixel_data[y][x].lstrip('#')
                rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
                img.putpixel((x, y), rgb)

        img = img.resize((self.grid_size * self.cell_size, self.grid_size * self.cell_size), Image.NEAREST)
        img.save(file_path)
        print(f"Saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PixelEditor(root)
    root.mainloop()
