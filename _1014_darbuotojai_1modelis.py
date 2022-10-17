# Sukurti programą, kuri:
#     Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba
#  (data būtų nustatoma automatiškai, pagal dabartinę datą).
#     Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
#     Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/darbuotojai4.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'Darbuotojai'
    id = Column(Integer, primary_key=True)
    name = Column("Vardas", String)
    surname = Column("Pavardė", String)
    birthday = Column("Gimimo data", Date)
    position = Column("Pareigos", String)
    salary = Column("Atlyginimas", Float)
    year = Column("Dirba nuo", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, birthday, position, salary):
        self.name = name
        self.surname = surname
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")
        self.position = position
        self.salary = salary
    
    def __repr__(self):
        return f"({self.id}, {self.name}, {self.surname}, {self.birthday}, {self.position}, {self.salary}, {self.year})"

if __name__ == "__main__":
    Base.metadata.create_all(engine)