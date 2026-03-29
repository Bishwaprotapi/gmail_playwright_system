import sqlite3
import csv


def export_csv():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT sender,subject,time FROM emails")

    rows = cursor.fetchall()

    with open("emails.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["Sender", "Subject", "Time"])

        for r in rows:
            writer.writerow(r)

    conn.close()

    print("CSV exported")