import csv
import sqlite3
from pathlib import Path

# Resolve paths relative to script location, not current working directory
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "../sample_data/users.csv"
DATABASE_FILE = BASE_DIR / "users.db"


def create_database():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    connection.commit()
    return connection


def read_csv_file():
    users = []
    with open(CSV_FILE, 'r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row.get("name", "").strip()
            email = row.get("email", "").strip()

            if name and email:
                users.append((name, email))

    return users


def insert_users(connection, users):
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT OR IGNORE INTO users (name, email)
        VALUES (?, ?)
    """, users)

    connection.commit()


def display_users(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email
        FROM users
    """)

    users = cursor.fetchall()

    print("\nUsers in Database:")
    print("-" * 60)
    for user in users:
        print(
            f'ID: {user[0]} | '
            f'Name: {user[1]} | '
            f'Email: {user[2]}'
        )
    print("-" * 60)
    print(f"Total users: {len(users)}")


def main():
    if not CSV_FILE.exists():
        print(f"CSV file not found: {CSV_FILE}")
        return

    users = read_csv_file()

    if not users:
        print("No valid users found in csv file.")
        return

    connection = create_database()
    insert_users(connection, users)
    display_users(connection)
    connection.close()


if __name__ == "__main__":
    main()
