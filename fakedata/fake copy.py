import sqlite3
from faker import Faker
import os

fake = Faker()
output_dir = 'generated_files'

os.makedirs(output_dir, exist_ok=True)

# connect to a new sqlite database (the file will be created)
conn = sqlite3.connect('new_test.db')
cursor = conn.cursor()

# create the table in the new db
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
               name TEXT,
               id_number INTEGER,
               birthday TEXT
               )
''')


# generate and insert 100 rows of data
for i in range (1, 101):
    name = fake.name()
    id_number = fake.unique.random_int(min=100000, max=999999)
    birthday = fake.date_of_birth(minimum_age=18, maximum_age = 90)

    # insert into db
    cursor.execute('''
    INSERT INTO users (name, id_number, birthday)
    VALUES (?, ?, ?)
    ''', (name, id_number, birthday))

    content = f"{name}\n{id_number}\n{birthday}\n"
    
    filename = f"user_{i:03}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        f.write(content)

conn.commit()
conn.close()

print ("100 files generated and added to test_db")       

