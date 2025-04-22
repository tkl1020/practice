import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
from faker import Faker
import os

# Set up the Faker object
fake = Faker()

def generate_fake_data(num_records, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Connect to a new sqlite database (or existing one)
    conn = sqlite3.connect(os.path.join(output_dir, 'test_db.db'))
    cursor = conn.cursor()

    # Create the table in the new db
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
                   name TEXT,
                   id_number INTEGER,
                   birthday TEXT
                   )
    ''')

    # Generate and insert fake data into DB and create text files
    for i in range(1, num_records + 1):
        name = fake.name()
        id_number = fake.unique.random_int(min=100000, max=999999)
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)

        # Insert into db
        cursor.execute('''
        INSERT INTO users (name, id_number, birthday)
        VALUES (?, ?, ?)
        ''', (name, id_number, birthday))

        # Create and save text file
        content = f"{name}\n{id_number}\n{birthday}\n"
        filename = f"user_{i:03}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w') as f:
            f.write(content)

    conn.commit()
    conn.close()

def browse_directory():
    # Let the user choose the output directory
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_dir_var.set(folder_selected)

def generate_data():
    # Get the number of records and output directory from UI
    try:
        num_records = int(num_records_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of records.")
        return

    output_dir = output_dir_var.get()
    if not output_dir:
        messagebox.showerror("Error", "Please select an output directory.")
        return

    # Generate the fake data
    generate_fake_data(num_records, output_dir)
    messagebox.showinfo("Success", f"{num_records} records generated and added to the database!")

# Set up the main application window
root = tk.Tk()
root.title("Fake Data Generator")

# Define variables
num_records_var = tk.StringVar()
output_dir_var = tk.StringVar()

# Create the UI components
tk.Label(root, text="Fake Data Generator", font=("Arial", 16)).pack(pady=10)

# Input field for the number of records
tk.Label(root, text="Number of records to generate:").pack(pady=5)
tk.Entry(root, textvariable=num_records_var).pack(pady=5)

# Browse button to select output directory
tk.Button(root, text="Select Output Directory", command=browse_directory, width=20).pack(pady=10)

# Display the selected output directory
tk.Label(root, textvariable=output_dir_var).pack(pady=5)

# Generate button to create the fake data
tk.Button(root, text="Generate Data", command=generate_data, width=20).pack(pady=20)

# Run the application
root.mainloop()