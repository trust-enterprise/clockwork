"""
OOP Class CLI Application

Features:
- Add / Update class
- Delete class
- Search class
- View classes (sorted)
- Generate unique random roll numbers
- Export to CSV
- Command-line arguments support
"""

import sqlite3
import random
import argparse
import csv
import sys


class SchoolDatabase:
    def __init__(self, db_name="school_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS school_classes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_name TEXT UNIQUE NOT NULL,
                strength INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_or_update_class(self, class_name, strength):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO school_classes (class_name, strength)
            VALUES (?, ?)
            ON CONFLICT(class_name)
            DO UPDATE SET strength = excluded.strength
        """, (class_name, strength))
        self.conn.commit()

    def delete_class(self, class_name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM school_classes WHERE class_name = ?", (class_name,))
        self.conn.commit()

    def search_class(self, class_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM school_classes WHERE class_name = ?", (class_name,))
        return cursor.fetchone()

    def get_all_classes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT class_name, strength FROM school_classes ORDER BY class_name ASC")
        return cursor.fetchall()

    def get_strength(self, class_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT strength FROM school_classes WHERE class_name = ?", (class_name,))
        result = cursor.fetchone()
        return result[0] if result else None

    def export_to_csv(self, filename="classes_export.csv"):
        data = self.get_all_classes()
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Class Name", "Strength"])
            writer.writerows(data)

    def close(self):
        self.conn.close()


class RollNumberGenerator:
    def __init__(self, strength):
        self.strength = strength
        self.generated = set()

    def generate(self):
        if len(self.generated) == self.strength:
            print("All roll numbers generated!")
            return None

        while True:
            roll = random.randint(1, self.strength)
            if roll not in self.generated:
                self.generated.add(roll)
                return roll


class SchoolCLI:
    def __init__(self):
        self.db = SchoolDatabase()

    def menu(self):
        while True:
            print("\n--- School CLI ---")
            print("1. Add / Update Class")
            print("2. Delete Class")
            print("3. Search Class")
            print("4. View All Classes")
            print("5. Generate Random Roll Numbers")
            print("6. Export to CSV")
            print("7. Exit")

            choice = input("Select option: ")

            if choice == "1":
                self.add_class()
            elif choice == "2":
                self.delete_class()
            elif choice == "3":
                self.search_class()
            elif choice == "4":
                self.view_classes()
            elif choice == "5":
                self.generate_roll()
            elif choice == "6":
                self.db.export_to_csv()
                print("Exported successfully!")
            elif choice == "7":
                self.db.close()
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid option.")

    def add_class(self):
        name = input("Class name: ").strip().upper()
        try:
            strength = int(input("Strength: "))
            self.db.add_or_update_class(name, strength)
            print("Saved successfully!")
        except ValueError:
            print("Enter valid number.")

    def delete_class(self):
        name = input("Class name to delete: ").strip().upper()
        self.db.delete_class(name)
        print("Deleted if existed.")

    def search_class(self):
        name = input("Class name to search: ").strip().upper()
        result = self.db.search_class(name)
        if result:
            print(f"{result[1]} has {result[2]} students")
        else:
            print("Class not found.")

    def view_classes(self):
        classes = self.db.get_all_classes()
        for cls in classes:
            print(f"{cls[0]} - {cls[1]} students")

    def generate_roll(self):
        name = input("Class name: ").strip().upper()
        strength = self.db.get_strength(name)

        if strength:
            generator = RollNumberGenerator(strength)
            while True:
                roll = generator.generate()
                if roll:
                    print(f"Roll No: {roll}")
                else:
                    break

                more = input("More? (y/n): ").lower()
                if more != "y":
                    break
        else:
            print("Class not found.")


def parse_arguments():
    parser = argparse.ArgumentParser(description="School CLI Application")
    parser.add_argument("--view", action="store_true", help="View all classes")
    parser.add_argument("--export", action="store_true", help="Export to CSV")
    return parser.parse_args()


def main():
    args = parse_arguments()
    cli = SchoolCLI()

    if args.view:
        cli.view_classes()
    elif args.export:
        cli.db.export_to_csv()
        print("Exported successfully!")
    else:
        cli.menu()


if __name__ == "__main__":
    main()
