import sqlite3

connection = sqlite3.connect('sqlite3.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS todolist')

create_table_query = """
    CREATE TABLE IF NOT EXISTS todolist(
        id INTEGER primary key AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status BOOLEAN DEFAULT FALSE
    );
"""

connection.execute(create_table_query)
connection.commit()
connection.close()
