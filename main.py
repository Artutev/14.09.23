import psycopg2
from psycopg2 import sql

db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'your_database_name',
    'user': 'postgres',
    'password': 'your_postgres_password'
}

connection = psycopg2.connect(**db_params)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
"""

cursor.execute(create_table_query)

insert_data_query = """
INSERT INTO users (username, email) VALUES (%s, %s);
"""

user_data = ('JohnDoe', 'johndoe@example.com')
cursor.execute(insert_data_query, user_data)

select_data_query = """
SELECT * FROM users;
"""

cursor.execute(select_data_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
cursor.close()
connection.close()
