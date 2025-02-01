import sqlite3

class DatabaseManager:
    def __init__(self, db_name='test.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
    
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                access_level TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                purchase_history TEXT
            )
        """)
        self.connection.commit()
    
    def close(self):
        self.connection.close()
    
    def find_user_by_name(self name):
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.cursor.fetchone()
    
    def execute_transaction(self, operations):
        try:
            for operation in operations:
                self.cursor.execute(*operation)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Ошибка транзакции:", e)

class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def add_user(self, name, email, age)
        self.db_manager.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        self.db_manager.connection.commit()
    
    def get_user(self, user_id):
        self.db_manager.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return self.db_manager.cursor.fetchone()
    
    def delete_user(self, user_id):
        self.db_manager.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db_manager.connection.commit()

class Admin(User):
    def add_admin(self, name, email, age, access_level):
        self.db_manager.cursor.execute("INSERT INTO admins (name, email, age, access_level) VALUES (?, ?, ?, ?)", (name, email, age, access_level))
        self.db_manager.connection.commit()
    
    def get_admin(self, admin_id):
        self.db_manager.cursor.execute("SELECT * FROM admins WHERE id = ?", (admin_id,))
        return self.db_manager.cursor.fetchone()

class Customer(User):
    def add_customer(self, name, email, age, purchase_history):
        self.db_manager.cursor.execute("INSERT INTO customers (name, email, age, purchase_history) VALUES (?, ?, ?, ?)", (name, email, age, purchase_history))
        self.db_manager.connection.commit()
    
    def get_customer(self, customer_id):
        self.db_manager.cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        return self.db_manager.cursor.fetchone()
    
if __name__ == "__main__":
    db = DatabaseManager("gmail.db")
    user_manager = User(db)
    admin_manager = Admin(db)
    customer_manager = Customer(db)
    
    user_manager.add_user("Хасан", "hasan@gmail.com", 16)
    admin_manager.add_admin("Али", "ali@gmail.com", 16, "admin")
    customer_manager.add_customer("акбар", "akbar@gmail.com", 18, "qwerty")
    
    print(user_manager.get_user(1))
    print(admin_manager.get_admin(1))
    print(customer_manager.get_customer(1))
    
    db.close()
