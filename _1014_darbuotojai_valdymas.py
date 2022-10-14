# Sukurti programą, kuri:
#     Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba
#  (data būtų nustatoma automatiškai, pagal dabartinę datą).
#     Duomenys būtų saugomi duomenų bazėje, panaudojant SQLAlchemy ORM (be SQL užklausų)
#     Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.
# 
# Perdaryti programą 1 užduotyje, kad ji:
#
#     Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Tkinter
#     Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
#     Parodytų visų į duomenų bazę įvestų asmenų sąrašą
#     Leistų ištrinti pasirinktą asmenį iš duomenų bazės
#     Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę Sukurti paleidžiamąjį programos failą (exe, su ikona)


from _1014_darbuotojai_modelis import Darbuotojai, engine
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
        # birthday = input("Gimimo data: ") kaip čia su tomis datomis????
        position = input("Pareigos: ")
        salary = float(input("Atlyginimas: "))
    except ValueError:
        print("KLAIDA: Atlyginimas nurodomas skaičiais")
        # year = input("Dirba nuo: ") kaip čia su tomis datomis????
    except ValueError:
        print("KLAIDA: Dirba nuo turi būti skaičius.")
        return
    else:
        employee = Darbuotojai(name, surname, birthday, position, salary, year)
        session.add(employee)
        session.commit()
        print(f"Darbuotojas {employee} sukurtas sėkmingai!")

def update_employee():
    pass

def delete_employee():
    pass


# programos MENIU
while True:
    print("=== Darbuotojų duomenų bazė ===")
    print("Pasirinkite: ")
    print("- q: išeiti")
    print("- p: rodyti visus darbuotojus")
    print("- n: naujas darbuotojas")
    print("- u: pakeisti darbuotojo duomenis")
    print("- d: trinti darbuotoją")
    pasirinkimas = input("Pasirinkite: ").casefold()
    if pasirinkimas == "q":
        print("Programa baigta!")
        break
    elif pasirinkimas == "p":
        print_list()
    elif pasirinkimas == "n":
        new_employee()
    elif pasirinkimas == "u":
        update_employee()
    elif pasirinkimas == "d":
        delete_employee()
    else:
        print("KLAIDA: Blogas pasirinkimas, rinkitės iš naujo!")
