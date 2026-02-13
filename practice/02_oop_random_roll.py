import sys
import sqlite3
import random

class Lab_Manager:
    def __init__(self, db_name = "batch_2025.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                       CREATE TABLE IF NOT EXISTS classes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       class TEXT UNIQUE NOT NULL,
                       strength INTEGER NOT NULL
                       )''')
        self.conn.commit() 

    def get_class_strength(self, class_name): 
        self.cursor.execute('''
                       SELECT strength FROM classes WHERE class = ?
                       ''',(class_name,))
        result_strength = self.cursor.fetchone()
        return result_strength[0] if result_strength else None

    def generate_random_roll(self, strength):
        roll_no = random.randint(1, strength)
        print(f"Random roll number is: {roll_no}")

    def update_class(self, class_name, strength): 
        self.cursor.execute('''
                            INSERT INTO classes (class, strength) VALUES(?,?)
                            ON CONFLICT (class) DO UPDATE SET strength = excluded.strength
                            ''', (class_name, strength))
        self.conn.commit()
        return class_name, strength
        
    def view_classes(self): 
        self.cursor.execute('''
                       SELECT class, strength FROM classes ORDER BY class ASC
                       ''')
        result_all_classes = self.cursor.fetchall()
        return result_all_classes

    def run(self):

        while True:
            print(f"\n1. generate random roll no.")
            print("2. add/update class")
            print("3. view all classes")
            print("4. exit")

            choice = input("select a number: ").strip()
            if choice == "1":
                class_name  = input("enter class: ").strip().upper()
                strength = self.get_class_strength(class_name)

                if strength and strength>0:
                    self.generate_random_roll(strength)

                    more = input("want more random rolls? (y/n) ").strip().lower()
                    while more == "y":    
                        self.generate_random_roll(strength)
                        more = input("want more random rolls? (y/n) ").strip().lower()
                        
                else:
                    print("class not found")
            
            elif choice == "2":
                class_name  = input("enter class: ").strip().upper()
                try:
                    strength = int(input("enter class strength: "))
                    saved_class, saved_strength = self.update_class(class_name, strength)
                    print(f"[Success] {saved_class} has {saved_strength} students.")
                except ValueError:
                    print("[Error] enter valid number for strength")
                
            elif choice == "3":
                result = self.view_classes()
                for row in result:
                    print(f"class {row[0]} : {row[1]} students")
                    
            elif choice == "4":
                print("good bye")
                self.conn.close()
                sys.exit()
            else:
                print("enter a valid number")

if __name__ == "__main__":
    lab = Lab_Manager()
    lab.run()