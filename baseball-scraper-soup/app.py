import requests
from bs4 import BeautifulSoup
import sqlite3

# Step 1: Scrape data from Baseball Reference
url = "https://www.baseball-reference.com/leagues/MLB/2023-standard-batting.shtml"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# The actual table is inside an HTML comment, so we extract it that way

from bs4 import Comment

comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(f"Found {len(comments)} comments")

# Optional: Print first few characters of the first 2 comments
for i, c in enumerate(comments[:2]):
    print(f"\n--- Comment #{i} ---")
    print(c[:500])  # Show first 500 chars

from bs4 import Comment

for comment in comments:
    if 'players_standard_batting' in comment.lower():
        table_soup = BeautifulSoup(comment, 'html.parser')
        break

if table_soup is None:
    raise Exception("Could not find the players_standard_batting table in the page.")

table = table_soup.find('table')
headers = [th.text for th in table.find('thead').find_all('th')][1:]  # skip rank column

rows = []
for row in table.find('tbody').find_all('tr'):
    if row.get('class') and 'thead' in row.get('class'):
        continue  # skip subheaders
    cells = row.find_all('td')
    if not cells:
        continue
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Step 2: Create SQLite database and insert data
conn = sqlite3.connect('mlb_batting_stats_2023.db')
c = conn.cursor()

# Create table
columns = ', '.join([f'"{header}" TEXT' for header in headers])
c.execute(f'CREATE TABLE IF NOT EXISTS batting_stats ({columns})')

# Insert data
placeholders = ', '.join(['?'] * len(headers))
c.executemany(f'INSERT INTO batting_stats VALUES ({placeholders})', rows)

conn.commit()
conn.close()
print("Data saved to mlb_batting_stats_2023.db")