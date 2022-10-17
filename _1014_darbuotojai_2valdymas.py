# Sukurti programą, kuri:
#     Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba
#  (data būtų nustatoma automatiškai, pagal dabartinę datą).
#     Duomenys būtų saugomi duomenų bazėje, panaudojant SQLAlchemy ORM (be SQL užklausų)
#     Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
# 


import datetime
from _1014_darbuotojai_1modelis import Darbuotojai, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

def print_list():
    print("---Darbuotojai---")
    print("(#, Vardas, Pavardė, Gimimo data, Pareigos, Atlyginimas, Dirba nuo)")
    employees = session.query(Darbuotojai).all()
    for employee in employees:
        print(employee)

def new_employee():
    print("--- Naujas darbuotojas ---")
    try:
        name = str(input("Vardas: "))
        surname = str(input("Pavardė: "))
        birthday = input("Gimimo data YYYY-MM-DD HH:MM:SS: ") 
        position = input("Pareigos: ")
        salary = float(input("Atlyginimas: "))
    except ValueError:
        print("KLAIDA: Atlyginimas nurodomas skaičiais")
        return
    else:
        employee = Darbuotojai(name, surname, birthday, position, salary)
        session.add(employee)
        session.commit()
        print(f"Darbuotojas {employee} sukurtas sėkmingai!")

def input_employee():
    print_list()
    try:
        employee_id = int(input("Įveskite trinamo/keičiamo darbuotojo ID: "))
    except ValueError:
        print("KLAIDA: ID turi būti skaičius")
        return None
    else:
        if employee_id:
            employee = session.query(Darbuotojai).get(employee_id)
            if employee:
                return employee
            else:
                print(f"KLAIDA: Darbuotojas su ID: {employee_id} neegzistuoja")
                return None

def update_employee():
    employee = input_employee()     
    if employee:
        try:
            name = input(f"Vardas ({employee.name}): ")
            surname = input(f"Pavardė ({employee.surname}): ")
            birthday = input(f"Gimimo data YYYY-MM-DD HH:MM:SS ({employee.birthday}): ")
            position = input(f"Pareigos ({employee.position}): ")
            salary = float(input(f"Atlyginimas ({employee.salary}): ") or 0)
        except ValueError:
            print("KLAIDA: Atlyginimas nurodomas skaičiais.")
            return
        else:
            if len(name) > 0:
                employee.name = name
            if len(surname) > 0:
                employee.surname = surname
            if birthday:
                employee.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")
            if len(position) > 0:
                employee.position = position
            if salary:
                employee.salary = salary
            session.commit()
            print(f"Darbuotojas {employee} atnaujintas sėkmingai.")  

def delete_employee():
    trinamas = input_employee()
    if trinamas:
        session.delete(trinamas)
        session.commit()
        print(f"Darbuotojas {trinamas} ištrintas sėkmingai!")

# programos MENIU
# while True:
#     print("=== Darbuotojų duomenų bazė ===")
#     print("Pasirinkite: ")
#     print("- q: išeiti")
#     print("- p: rodyti visus darbuotojus")
#     print("- n: naujas darbuotojas")
#     print("- u: pakeisti darbuotojo duomenis")
#     print("- d: trinti darbuotoją")
#     pasirinkimas = input("Pasirinkite: ").casefold()
#     if pasirinkimas == "q":
#         print("Programa baigta!")
#         break
#     elif pasirinkimas == "p":
#         print_list()
#     elif pasirinkimas == "n":
#         new_employee()
#     elif pasirinkimas == "u":
#         update_employee()
#     elif pasirinkimas == "d":
#         delete_employee()
#     else:
#         print("KLAIDA: Blogas pasirinkimas, rinkitės iš naujo!")
