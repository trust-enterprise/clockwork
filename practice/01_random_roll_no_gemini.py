# To make it impressive:
# Add sort in view
# Avoid no. repetition
# Add delete class option
# Add search option
# Add export to CSV
# Add unit tests
# Convert to OOP version
# Add command-line arguments (argparse)

"""
Class CLI Application

This program allows users to:
- Add or update class strength
- Generate random roll numbers (Continuously as much as required)
- View all stored classes

Data is stored in a SQLite database (school_data.db).
"""

import sqlite3
import random
import sys

def init_db():
    conn = sqlite3.connect("school_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS school_classes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   class_name TEXT UNIQUE NOT NULL,
                   strength INTEGER NOT NULL
                   ) 
                   """)
    conn.commit()
    return conn

def update_class(conn, class_name, strength):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO school_classes (class_name, strength) 
                   VALUES (?,?)
                   ON CONFLICT (class_name) DO UPDATE SET strength = excluded.strength
                   ''', (class_name, strength))
    conn.commit()
    return True

def get_strength(conn, class_name):
    """
    Fetch the strength of a given class.

    Args:
        conn (sqlite3.Connection): Active database connection.
        class_name (str): Name of the class.

    Returns:
        int | None: Strength if class exists, otherwise None.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT strength FROM school_classes WHERE class_name = ?', (class_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def random_roll_no(strength):
    roll_no = random.randint(1, strength)
    print(f"Random roll no.: {roll_no}")
    

def main():
    conn = init_db()

    while True:
        print("\n--- Computer Lab CLI ---")
        print("1. Add/Edit Class Strength")
        print("2. Generate Random Roll Number")
        print("3. View All Classes")
        print("4. Exit")
        
        choice = input("select an option: ")

        if choice == "1":
            class_name = input("which class: ").strip().upper()
            try:
                class_strength = int(input("enter strength: "))
                update_class(conn, class_name, class_strength)
                print(f"\n[Success] {class_name} has {class_strength} students")
            except ValueError:
                print("[Error] enter valid number for class strength")
        
        elif choice == "2":
            class_name = input("which class: ").strip().upper()
            strength = get_strength(conn, class_name)
            if strength is not None and strength > 0:
                random_roll_no(strength)

                #print more random roll nos
                more_roll_nos = input('want more roll nos? (y/n)').strip().lower()

                while (more_roll_nos == "y"):
                    random_roll_no(strength)
                    more_roll_nos = input('want more roll nos? (y/n)').strip().lower()
            else:
                print(f"[Error] class not found")
        
        elif choice == "3":
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM school_classes')
            result = cursor.fetchall()

            for row in result:
                print(f"{row[1]} has {row[2]} students")
        
        elif choice == "4":
            print("good bye!")
            conn.close()
            sys.exit()
        
        else:
            print('select a valid option. try again')


if __name__ == "__main__":
    main()