#Step 0 - importsqlite3
import sqlite3
import queries as q

#Step 1
#Conntect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

#Step 2
cursor = connection.cursor()

#Step 3
query = 'SELECT * FROM charactercreator_character;'

#Step 4
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])