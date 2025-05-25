from config import conn, cursor

class Employee:
    def __init__(self, first_name, last_name, email, phone_number, gender, position, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.gender = gender
        self.position = position
        self.id = id

    # SQL query to create the employee database table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone_number TEXT,
                gender TEXT,
                position TEXT
            );
        """
        cursor.execute(sql)
        conn.commit()

   # @classmethod
    #def frop_table(cls):
        #sql = "DROP TABLE IF EXISTS employee;"

        #cursor.execute(sql)
        #conn.commit()

# To create the table, you can call:
# Employee.create_table()
