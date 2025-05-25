import sqlite3


# create a connection to the db
conn = sqlite3.connect("moringa.db")

#cursor to execute statements
cur = conn.cursor()
class Customer:
    TABLE_NAME = "customers"
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        sql = """
            INSERT INTO {self.TABLE_NAME} (name, phone)
            VALUES (?, ?) 
        """

        cur.execute(sql, {self.name, self.phone})
        conn.commit()
        print(f"{self.name} inserted successfully")

    @classmethod
    def create_table(cls):
        sql =  """
        CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE
        );
        """

        cur.execute(sql)
        #persists changes to the db
        conn.commit
        print("Customer table created")
    
Customer.create_table()

Customer1 = Customer("Nancy", "0787654321")
Customer1.save