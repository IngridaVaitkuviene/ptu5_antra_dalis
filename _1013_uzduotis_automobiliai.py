# 1. Sukurkite duomenų bazę, kurioje būtų lentelė su automobilio marke, modeliu, spalva, pagaminimo metais, ir kaina.
# 2. Parašykite programą, kuri leistų vartotojui per konsolę: 
#       įvesti naują eilutę (automobilį su visais parametrais);
#       ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti. 
#       Metus ir kainą vartotojas turėtų nurodinėti nuo - iki.

import sqlite3

connector = sqlite3.connect('data/auto.db')
cursor = connector.cursor()
# 1.
# query = '''
# CREATE TABLE IF NOT EXISTS auto (
#     make VARCHAR(50),
#     model VARCHAR(50),
#     color VARCHAR(50),
#     year INTEGER,
#     price INTEGER
# );
# '''
# cursor.execute(query)
# connector.commit()
# connector.close()

# 2.
with connector:
    while True:
        car = input("Įveskite auto markę arba q, kad išeiti arba n kad įvesti naują: ")
        if car.casefold() == "q":
            break
        elif car.casefold() == "n":
            print("--- NEW car ---")
            new_make = input("Gamintojas: ")
            new_model = input("Modelis: ")
            new_color = input("Spalva: ")
            new_year = input("Pagaminimo metai: ")
            new_price = float(input("Kaina: "))
            cursor.execute('INSERT INTO auto (make, model, color, year, price) VALUES (?, ?, ?, ?, ?)',
                (new_make, new_model, new_color, new_year, new_price))
            connector.commit()
        else:
            select_query = f'SELECT * FROM auto WHERE make LIKE ?'
            cursor.execute(select_query, (f'%{car}%', ))
            rezultatas = cursor.fetchall()
            if rezultatas:
                print("Vykdant paiešką surasta: ")
                for auto in rezultatas:
                    print(f"- {auto[0]} {auto[1]} ({auto[3]})")
            else:
                print("Tokio automobilio nerasta")
    print("Programos pabaiga.")