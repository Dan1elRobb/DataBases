import sqlite3
from faker import Faker
import random
conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
insert = '''
INSERT INTO
    students (firstname, lastname, age, gender)
VALUES
    ('Hermione', 'Grainger', 14, 'Female') ;
'''
param_insert = '''
INSERT INTO
    students (firstname, lastname, age, gender)
VALUES
    (?,?,?,?);
'''
fake = Faker('en_GB')
random.seed(1234567)
fake.random.seed(1234567)
for _ in range(100):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11,18)
    gender = random.choice(('male','female'))
    cursor.execute(param_insert,
                   (f_name, l_name, age, gender))
conn.commit()


update = '''
UPDATE students
SET lastname = ?
WHERE id = 4;
'''
cursor.execute(update, ('Smith',))
cursor.execute(insert)
cursor.execute(param_insert, ('Harry', 'Potter', 13, 'Male'))
conn.commit()
conn.close()