from faker import Faker
import os

fake = Faker()
output_dir = 'generated_files'

os.makedirs(output_dir, exist_ok=True)

for i in range (1, 101):
    name = fake.name()
    id_number = fake.unique.random_int(min=100000, max=999999)
    birthday = fake.date_of_birth(minimum_age=18, maximum_age = 90)

    content = f"Name: {name}\nID: {id_number}\nBirthday: {birthday}\n"
    
    filename = f"user_{i:03}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        f.write(content)

print ("100 files generated")       

