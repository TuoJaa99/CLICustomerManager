import sqlite3
import main
import menus
from time import sleep

#add a new customer to the db

def add_customer():
    name = input("Customer Name: ").strip()
    owned_int = input("Amount to add: ").strip()

    try:
        owned = float(owned_int)
    except ValueError:
        print("Invalid format, use numbers!")
        return

    conn = sqlite3.connect('asiakkaat.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            owned FLOAT 
        )
    ''')

    cursor.execute('''
        INSERT INTO customers (name, owned)
        VALUES (?, ?)
    ''', (name, owned))

    conn.commit()
    conn.close()
    print(f"Customer '{name}' added to database with amount {owned}!")


def add_to_existing():
    name = input("Customer name: ").strip()
    owned_int = input("Amount: ").strip()

    try:
        owned = float(owned_int)
    except ValueError:
        print("Invalid format")
        return

    conn = sqlite3.connect('asiakkaat.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT owned FROM customers WHERE name = ?
        ''', (name, ))
    customer = cursor.fetchone()

    if customer:
        new_amount = customer[0] + owned
        cursor.execute('''
                       UPDATE customers SET owned = ? WHERE name = ? 
                        ''', (new_amount, name))
        print(f"{owned} added to {name}")
    else:
        print(f"{name} not found or does not exist")
    conn.commit()
    conn.close()


def delete_customer():
    conn = sqlite3.connect('asiakkaat.db')
    cursor = conn.cursor()

    name = input("Who to delete: ").strip()

    cursor.execute('SELECT * FROM customers WHERE name = ?', (name,))
    customer = cursor.fetchone()
    print(f"Do you really want to delete {name}?")
    print("1 = yes 2 = no")
    nav = input(": ")
    while True:
        if nav == "1":
            if customer:
                cursor.execute('DELETE FROM customers WHERE name = ?', (name,))
                conn.commit()
                print(f"{name} has been deleted")
                sleep(2)
                menus.clear()
                main.main()
            else:
                print(f"{name} not found in database")
                break
                menus.clear()
                main.main()
            

        if nav == "2":
            menus.clear()
            main.main()
    conn.close()

def print_table():
    conn = sqlite3.connect('asiakkaat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()





if __name__ == "__main__":
    main.main()
