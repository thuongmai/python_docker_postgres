import psycopg2
from sql_command import *

# Connect to an existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0",
)

# Make sure the insert will commit to the table
conn.autocommit = True

# Open cursor to perform database operations
cur = conn.cursor()

try:
    cur.execute(create_table)

    # Insert data
    for insert_data in insert_data_group:
        cur.execute(insert_data)
    # An alternative way to commit, but this one has to add everytime we insert/update/delete the record to commit to table
    # conn.commit()

    # Query the database
    cur.execute(select_data)
    rows = cur.fetchall()

    if not len(rows):
        print("Empty")
    else:
        for row in rows:
            print(row)

except Exception as e:
    print(e)
finally:
    # Close communication with database
    cur.close()
    conn.close()
