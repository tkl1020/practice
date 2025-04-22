import tkinter as tk
import time
import threading
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows
init(autoreset=True)

# ASCII flag base
flag_lines = [
    "★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆        █████████████████████████",
    "☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★        █████████████████████████",
    "★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆        █████████████████████████",
    "☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★        █████████████████████████",
    "★ ☆ ★ ☆ ★ ☆ ★ ☆ ★ ☆        █████████████████████████",
    "                          █████████████████████████",
    "                          █████████████████████████",
    "                          █████████████████████████",
    "                          █████████████████████████",
    "                          █████████████████████████",
]

# Simple color cycling
def colorize_line(line, shift):
    colored = ""
    for i, char in enumerate(line):
        if char in ["★", "☆"]:
            colored += Fore.BLUE + char
        elif char == "█":
            color = Fore.RED if (i + shift) % 2 == 0 else Fore.WHITE
            colored += color + char
        else:
            colored += " "
    return colored

# Flag animation logic
def animate_flag(text_widget):
    shift = 0
    while True:
        text_widget.delete("1.0", tk.END)
        for line in flag_lines:
            wave = line[shift:] + line[:shift]
            colored = colorize_line(wave, shift)
            text_widget.insert(tk.END, colored + "\n")
        shift = (shift + 1) % len(flag_lines[0])
        time.sleep(0.1)

# Create a separate window with black background
def create_flag_window():
    root = tk.Tk()
    root.title("ASCII Flag - Waving in the Wind 🇺🇸")
    root.configure(bg="black")

    text = tk.Text(root, bg="black", fg="white", font=("Courier", 12), spacing3=2)
    text.pack(expand=True, fill="both")

    # Run the flag animation in a separate thread
    thread = threading.Thread(target=animate_flag, args=(text,), daemon=True)
    thread.start()

    root.mainloop()

if __name__ == "__main__":
    create_flag_window()
