# Perdaryti programą 1 užduotyje, kad ji:
#
#     Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Tkinter
#     Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
#     Parodytų visų į duomenų bazę įvestų asmenų sąrašą
#     Leistų ištrinti pasirinktą asmenį iš duomenų bazės
#     Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę.
#     Sukurti paleidžiamąjį programos failą (exe, su ikona)

from datetime import date
from tkinter import *
from _1014_darbuotojai_2valdymas import *

# langas
langas = Tk()
langas.geometry("1000x600")
langas.title("Darbuotojų sąrašo administravimas v1.0")
ikonele = PhotoImage(file="image/package.png")
langas.iconphoto(True, ikonele)

def darbuotojo_ivedimas():
    ivesta_vardas = laukas_vardas.get()
    ivesta_pavarde = laukas_pavarde.get()
    ivesta_gimtadienis = laukas_gimtadienis.get()
    ivesta_pareigos = laukas_pareigos.get()
    ivesta_atlyginimas = laukas_atlyginimas.get()
    laukas_vardas.delete(0, len(ivesta_vardas))
    laukas_pavarde.delete(0, len(ivesta_pavarde))
    laukas_gimtadienis.delete(0, len(ivesta_gimtadienis))
    laukas_pareigos.delete(0, len(ivesta_pareigos))
    laukas_atlyginimas.delete(0, len(ivesta_atlyginimas))
    darbuotojas = Darbuotojai(ivesta_vardas, ivesta_pavarde, ivesta_gimtadienis, ivesta_pareigos, ivesta_atlyginimas)
    session.add(darbuotojas)
    session.commit()

def darbuotoju_sarasas():
    employees = session.query(Darbuotojai).all()
    for employee in employees:
        boxas.insert(END, employee)

def isvalyti_sarasa():
    employees = session.query(Darbuotojai).all()
    boxas.delete(0, len(employees))

def darbuotojo_redagavimas():
    darbuotojo_id = laukas_trinimui.get()
    darbuotojas = session.query(Darbuotojai).get(darbuotojo_id)
    vardas = laukas_redag_vardas.get()
    pavarde = laukas_redag_pavarde.get()
    gimtadienis = laukas_redag_gimtadienis.get()
    pareigos = laukas_redag_pareigos.get()
    atlyginimas = laukas_redag_atlyginimas.get()
    if len(vardas) > 0:
        darbuotojas.vardas = vardas
    if len(pavarde) > 0:
        darbuotojas.pavarde = pavarde
    if gimtadienis:
        darbuotojas.gimtadienis = datetime.datetime.strptime(gimtadienis, "%Y-%m-%d")
    if len(pareigos) > 0:
        darbuotojas.pareigos = pareigos
    if atlyginimas:
        darbuotojas.atlyginimas = atlyginimas
    session.commit()
    laukas_trinimui.delete(0, len(darbuotojo_id))
    laukas_redag_vardas.delete(0, len(vardas))
    laukas_redag_pavarde.delete(0, len(pavarde))
    laukas_redag_gimtadienis.delete(0, len(gimtadienis))
    laukas_redag_pareigos.delete(0, len(pareigos))
    laukas_redag_atlyginimas.delete(0, len(atlyginimas))

def darbuotojo_istrinimas():
    darbuotojo_id = laukas_trinimui.get()
    darbuotojas = session.query(Darbuotojai).get(darbuotojo_id)
    session.delete(darbuotojas)
    session.commit()
    laukas_trinimui.delete(0, len(darbuotojo_id))

# uzrasai
uzrasas_ivesti = Label(langas, text="Įveskite darbuotoją:")
uzrasas_vardas = Label(langas, text="Vardas: ")
uzrasas_pavarde = Label(langas, text="Pavardė: ")
uzrasas_gimtadienis = Label(langas, text="Gimimo data: ")
uzrasas_pareigos = Label(langas, text="Pareigos: ")
uzrasas_atlyginimas = Label(langas, text="Atlyginimas: ")
uzrasas_redaguoti = Label(langas, text="Redaguoti darbuotoją:")
uzrasas_trinti = Label(langas, text="Pasirinkite darbuotojo ID:")
uzrasas_redag_vardas = Label(langas, text="Vardas: ")
uzrasas_redag_pavarde = Label(langas, text="Pavardė: ")
uzrasas_redag_gimtadienis = Label(langas, text="Gimimo diena:")
uzrasas_redag_pareigos = Label(langas, text="Pareigos: ")
uzrasas_redag_atlyginimas = Label(langas, text="Atlyginimas: ")

# laukai ivedimui
laukas_vardas = Entry(langas)
laukas_pavarde = Entry(langas)
laukas_gimtadienis = Entry(langas)
laukas_pareigos = Entry(langas)
laukas_atlyginimas = Entry(langas)
laukas_trinimui = Entry(langas)
laukas_redag_vardas = Entry(langas)
laukas_redag_pavarde = Entry(langas)
laukas_redag_gimtadienis = Entry(langas)
laukas_redag_pareigos = Entry(langas)
laukas_redag_atlyginimas = Entry(langas)

# box'as pažiūrėjimui
uzrasas_boxui = Label(langas, text="Darbuotojų sąrašas:")
boxas_scroll = Scrollbar(langas)
boxas = Listbox(langas, yscrollcommand=boxas_scroll.set, width=100, selectmode=SINGLE)
boxas_scroll.config(command=boxas.yview)

# mygtukai
mygtukas_irasymo = Button(langas, text="Įrašyti", command=darbuotojo_ivedimas)
langas.bind("<Return>", lambda event: darbuotojo_ivedimas())
mygtukas_rodyti = Button(langas, text="Rodyti", command=darbuotoju_sarasas)
mygtukas_isvalyti = Button(langas, text="Išvalyti", command=isvalyti_sarasa)
mygtukas_trinimui = Button(langas, text="Ištrinti", command=darbuotojo_istrinimas)
mygtukas_redagavimo = Button(langas, text="Įrašyti pakeitimą", command=darbuotojo_redagavimas)

# grid'ai
uzrasas_ivesti.grid(row=0, column=0, sticky=W)
uzrasas_vardas.grid(row=1, column=0, sticky=W)
uzrasas_pavarde.grid(row=2, column=0, sticky=W)
uzrasas_gimtadienis.grid(row=3, column=0, sticky=W)
uzrasas_pareigos.grid(row=4, column=0, sticky=W)
uzrasas_atlyginimas.grid(row=5, column=0, sticky=W)
uzrasas_redaguoti.grid(row=11, column=0, sticky=W)
uzrasas_trinti.grid(row=12, column=0, sticky=W)
uzrasas_redag_vardas.grid(row=13, column=0, sticky=W)
uzrasas_redag_pavarde.grid(row=14, column=0, sticky=W)
uzrasas_redag_gimtadienis.grid(row=15, column=0, sticky=W)
uzrasas_redag_pareigos.grid(row=16, column=0, sticky=W)
uzrasas_redag_atlyginimas.grid(row=17, column=0, sticky=W)
uzrasas_boxui.grid(row=0, column=3, sticky=W)

laukas_vardas.grid(row=1, column=1)
laukas_pavarde.grid(row=2, column=1)
laukas_gimtadienis.grid(row=3, column=1)
laukas_pareigos.grid(row=4, column=1)
laukas_atlyginimas.grid(row=5, column=1)
laukas_trinimui.grid(row=12, column=1)
laukas_redag_vardas.grid(row=13, column=1)
laukas_redag_pavarde.grid(row=14, column=1)
laukas_redag_gimtadienis.grid(row=15, column=1)
laukas_redag_pareigos.grid(row=16, column=1)
laukas_redag_atlyginimas.grid(row=17, column=1)

mygtukas_irasymo.grid(row=6, column=1, ipadx=30)
mygtukas_rodyti.grid(row=10, column=3, ipadx=30, sticky=W)
mygtukas_isvalyti.grid(row=10, column=4, ipadx=30, sticky=W)
mygtukas_trinimui.grid(row=12, column=3, ipadx=30, sticky=W)
mygtukas_redagavimo.grid(row=18, column=1, ipadx=30, sticky=W)

boxas.grid(row=1, rowspan=9, column=3, columnspan=10, sticky=W)
boxas_scroll.grid(row=1, rowspan=9, column=13, ipady=50)

langas.mainloop()
