from db import init_db
import sqlite3

def add_patient(name, age, gender):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
    conn.commit()
    conn.close()

def view_patients():
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    init_db()
    add_patient("John Doe", 45, "Male")
    view_patients()
