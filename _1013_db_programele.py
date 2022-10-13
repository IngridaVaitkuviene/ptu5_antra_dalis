import sqlite3

connector = sqlite3.connect("data/zmones.db")
cursor = connector.cursor()

with connector:
    while True:
        vardas = input("Įveskite vardą arba q, kad išeiti: ")
        if vardas.casefold() == "q":
            break
        else:
            cursor.execute(f'SELECT * FROM draugai WHERE first_name LIKE "%{vardas}%"')
            rezultatas = cursor.fetchall()
            if rezultatas:
                print("Radau tokius draugelius: ")
                for draugas in rezultatas:
                    print(f"- {draugas[0]} {draugas[1]}")
            else:
                print("Tokio draugelio nėra")
    print("Bye!")