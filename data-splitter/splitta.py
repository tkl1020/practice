import sqlite3

#establish connection to sqlite db
conn = sqlite3.connect('testdb.db')
cursor = conn.cursor()

# path with the name, id, bd
file_path = 'C:\\Users\\Tom\\python practice\\generated_files\\user_001.txt'

# read data
with open(file_path, 'r') as file:
    # read the file's lines and strip any extra whitespace
    lines = [line.strip() for line in file.readlines()]

    # check is the file has at least 3 lines for name, id, bd
    if len(lines) >=3:
        name = lines[0]
        id_number = lines[1]
        birthday = lines[2]

        # prepare the SQL insert query
        insert_query = '''
        INSERT INTO test (random_id, name, birthday)
        VALUES (?, ?, ?)
        '''

        #insert the data into the table
        cursor.execute(insert_query, (id_number,name, birthday))

        #commit the transaction to save changes
        conn.commit()

        print("Data from file inserted into database successfully.")
    else:
        print("error retard alert")
conn.close()