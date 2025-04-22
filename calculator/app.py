import tkinter as tk


root = tk.Tk()
root.title("Basic Calculator")


# output display
display = tk.Entry(root,width=20, font=("Arial",24), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4) # grid layout for display in the top row


# digits (0-9) and operators (+, -, *, /)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda btn=button: on_button_click(btn)).grid(row=row, column=col)
    col += 1
    if col > 3:  # Move to the next row after 4 columns
        col = 0
        row += 1

def on_button_click(button):
    current = display.get() # get current display value            

    if button =="C":
        display.delete(0,tk.END) # clear the display
    elif button == "=":
        try:
            result = eval(current) # evaluate the expression in the display
            display.delete(0, tk.END)
            display.insert(tk.END, str(result)) # show the result
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button) # append the button pressed to the display

root.mainloop()


            