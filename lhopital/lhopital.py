import tkinter as tk
from tkinter import messagebox
import sympy as sp
import random

x = sp.Symbol('x')

# Random example expressions with limit points
EXAMPLES = [
    ("(sin(x))/x", 0),
    ("(1 - cos(x))/x**2", 0),
    ("ln(x)/x", sp.oo),
    ("x / exp(x)", sp.oo),
    ("(tan(x))/x", 0)
]

def apply_lhopital(expr_str, limit_point):
    try:
        expr = sp.sympify(expr_str)
        top = sp.numer(expr)
        bottom = sp.denom(expr)
        lim = sp.limit(expr, x, limit_point)

        steps = [f"Expression: {expr_str}",
                 f"Limit as x → {limit_point}: {lim}"]

        explanation = ""

        num_lim = sp.limit(top, x, limit_point)
        den_lim = sp.limit(bottom, x, limit_point)

        steps.append(f"Numerator → {num_lim}")
        steps.append(f"Denominator → {den_lim}")
        form = f"{num_lim}/{den_lim}"

        if (num_lim == 0 and den_lim == 0) or (num_lim.is_infinite and den_lim.is_infinite):
            explanation = "Because both the numerator and denominator approach 0 or ∞, this is an indeterminate form.\nWe apply L’Hôpital’s Rule by differentiating numerator and denominator."
            num_prime = sp.diff(top, x)
            den_prime = sp.diff(bottom, x)
            new_expr = num_prime / den_prime
            final_lim = sp.limit(new_expr, x, limit_point)
            steps.append(f"Apply L’Hôpital: ({num_prime}) / ({den_prime})")
            steps.append(f"New Limit: {final_lim}")
            steps.append("\nExplanation:")
            steps.append(explanation)
        else:
            explanation = "The limit is not indeterminate, so L’Hôpital’s Rule was not needed."
            steps.append("\nExplanation:")
            steps.append(explanation)

        return "\n".join(steps)
    except Exception as e:
        return f"Error: {e}"

def on_calculate():
    expr = entry_expr.get()
    try:
        point = float(entry_point.get()) if entry_point.get().lower() != 'oo' else sp.oo
    except ValueError:
        messagebox.showerror("Input Error", "Limit point must be a number (or 'oo' for infinity).")
        return
    result = apply_lhopital(expr, point)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

def on_randomize():
    expr, point = random.choice(EXAMPLES)
    entry_expr.delete(0, tk.END)
    entry_expr.insert(0, expr)
    entry_point.delete(0, tk.END)
    entry_point.insert(0, str(point))

# GUI Setup
root = tk.Tk()
root.title("L’Hôpital’s Rule Explorer")

tk.Label(root, text="Enter a rational expression (in x):").pack()
entry_expr = tk.Entry(root, width=40)
entry_expr.pack()
entry_expr.insert(0, "(sin(x))/x")

tk.Label(root, text="Enter limit point (use 'oo' for ∞):").pack()
entry_point = tk.Entry(root, width=10)
entry_point.pack()
entry_point.insert(0, "0")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Calculate Limit", command=on_calculate).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Random Example", command=on_randomize).pack(side=tk.LEFT, padx=5)

text_output = tk.Text(root, width=60, height=14, wrap="word")
text_output.pack(padx=10, pady=10)

root.mainloop()
