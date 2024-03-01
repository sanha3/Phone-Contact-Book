import sqlite3

# Function to create a new database table
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)''', (name, phone, email))
    conn.commit()
    conn.close()

# Function to fetch all data from the database
def fetch_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    rows = c.fetchall()
    conn.close()
    return rows

# Main function
if __name__ == "__main__":
    create_table()

    # Inserting 5 rows of data
    insert_data("sanha", "7583734890", "sanha@gmail.com")
    insert_data("firdose", "4356278908", "firdose@gmail.com")
    insert_data("sheikh", "2341567356", "sheikh@gmail.com")
    insert_data("megha", "9375892340", "megha@gmail.com")
    insert_data("varun", "9342763876", "varunb@gmail.com")

    # Fetching and displaying all data
    contacts = fetch_data()
    print("ID\tName\t\tPhone\t\tEmail")
    print("------------------------------------------")
    for contact in contacts:
        print(f"{contact[0]}\t{contact[1]}\t\t{contact[2]}\t{contact[3]}")
