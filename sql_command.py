create_table = """
        CREATE TABLE if not exists student (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER not null
        )
        """
insert_data_group = (
    "INSERT INTO student (name, age) VALUES ('Thunder',20)",
    "INSERT INTO student (name, age) VALUES ('Light',30)",
    "INSERT INTO student (name, age) VALUES ('Storm',40)",
    "INSERT INTO student (name, age) VALUES ('Tornado',50)",
)

select_data = "SELECT * from student"
