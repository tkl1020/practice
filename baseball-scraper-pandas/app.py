import tkinter as tk
from tkinter import messagebox
import pandas as pd
import sqlite3
import requests

def fetch_data(player_or_team, stat_var):
    url = "https://www.baseball-reference.com/leagues/MLB/2023-standard-batting.shtml"
    try:
        tables = pd.read_html(url)
        print(f"Found {len(tables)} tables")

        df = tables[0]  # Use the correct table index

        # If fetching player data, filter by player name or team
        if stat_var == "player":
            # Filter data by player name (case insensitive)
            player_data = df[df['Name'].str.contains(player_or_team, case=False)]
            if player_data.empty:
                messagebox.showerror("Error", "Player not found!")
                return
            print(player_data)

        elif stat_var == "team":
            # Filter data by team name (example)
            team_data = df[df['Tm'].str.contains(player_or_team, case=False)]
            if team_data.empty:
                messagebox.showerror("Error", "Team not found!")
                return
            print(team_data)

        # Save to SQLite
        conn = sqlite3.connect('mlb_batting_stats_2023.db')
        player_data.to_sql('batting_stats', conn, if_exists='replace', index=False)
        conn.close()
        print("Data saved to database!")

    except Exception as e:
        print(f"Error fetching data: {e}")
        messagebox.showerror("Error", "Failed to fetch data from website")

# Creating the UI for input
def submit_action():
    # Get the values from input fields
    player_or_team = player_entry.get()
    stat_var = stat_var_var.get()

    # Call the function to fetch and display stats
    fetch_data(player_or_team, stat_var)

# Creating the Tkinter app
root = tk.Tk()
root.title("MLB Stats Fetcher")

# Creating the UI elements
label = tk.Label(root, text="Enter Player or Team:")
label.pack(pady=10)

player_entry = tk.Entry(root)
player_entry.pack(pady=10)

# Radio buttons for selecting player or team
stat_var_var = tk.StringVar()
player_radio = tk.Radiobutton(root, text="Player", variable=stat_var_var, value="player")
player_radio.pack(pady=5)
team_radio = tk.Radiobutton(root, text="Team", variable=stat_var_var, value="team")
team_radio.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Fetch Stats", command=submit_action)
submit_button.pack(pady=20)

# Run the app
root.mainloop()
