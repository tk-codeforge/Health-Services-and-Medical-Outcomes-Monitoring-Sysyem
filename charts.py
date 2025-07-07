import matplotlib.pyplot as plt
import sqlite3

def plot_sugar_levels(patient_id):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, sugar FROM records WHERE patient_id = ?", (patient_id,))
    data = cursor.fetchall()
    dates, sugars = zip(*data)
    plt.plot(dates, sugars, marker='o')
    plt.title("Sugar Levels Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sugar Level")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
