import sqlite3


'''
student_index_no INT(48) NOT NULL,
student_name VARCHAR(255) NOT NULL,
number_of_school_days INT(300) NOT NULL,
number_of_present_days INT(300)
'''
x = 0

while x != 1:
    index_number = input('Index number: ')
    student_name = input('student name: ')

    number_of_school_days = 65
    sqliteConnection = sqlite3.connect('student.db')
    cursor = sqliteConnection.cursor()

    cursor.execute(f"INSERT INTO student VALUES({index_number}, '{student_name}', {number_of_school_days}, 50)")
    sqliteConnection.commit()
    cursor.close() 

    if(index_number == 48):
        x = 1


