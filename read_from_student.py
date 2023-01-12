import sqlite3
conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
select_students = '''
SELECT id, firstname, lastname
FROM students
WHERE age >= 13
'''
cursor.execute(select_students)
first_student = cursor.fetchone()
more_students = cursor.fetchmany(10)
other_students = cursor.fetchall()

print(first_student)
print(more_students)
print(other_students)