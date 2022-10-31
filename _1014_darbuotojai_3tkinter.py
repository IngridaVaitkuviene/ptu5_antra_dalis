# Perdaryti programą 1 užduotyje, kad ji:
#
#     Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Tkinter
#     Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
#     Parodytų visų į duomenų bazę įvestų asmenų sąrašą
#     Leistų ištrinti pasirinktą asmenį iš duomenų bazės
#     Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę.
#     Sukurti paleidžiamąjį programos failą (exe, su ikona)

from tkinter import *
from _1014_darbuotojai_2valdymas import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# langas
langas = Tk()
langas.geometry("1000x600")
langas.title("Darbuotojų sąrašo Nr. 4 administravimas v1.0")
ikonele = PhotoImage(file="image/package.png")
langas.iconphoto(True, ikonele)

pasirinktas_id = IntVar

# --------- Treeview lentele pradzia ----------- #
columns = ('id', 'name', 'surname', 'birthday', 'position', 'salary', 'year')

tree = ttk.Treeview(langas, columns=columns, show='headings', height=15)

tree.column('id', width=50)
tree.column('name', width=150)
tree.column('surname', width=150)
tree.column('birthday', width=100)
tree.column('position', width=210)
tree.column('salary', width=100)
tree.column('year', width=180)

tree.heading('id', text='id')
tree.heading('name', text='Vardas')
tree.heading('surname', text='Pavarde')
tree.heading('birthday', text='Gimimo metai')
tree.heading('position', text='Pareigos')
tree.heading('salary', text='Atlyginimas')
tree.heading('year', text='Dirba nuo')

darbuotoju_sarasas = []
darbuotojai = session.query(Darbuotojai).all()
for darbuotojas in darbuotojai:
    darbuotoju_sarasas.append((darbuotojas.id, 
    darbuotojas.name, darbuotojas.surname, 
    darbuotojas.birthday, darbuotojas.position,
    darbuotojas.salary, darbuotojas.year)
)

for darbuotojai in darbuotoju_sarasas:
    tree.insert('', END, values=darbuotojai)

# funkcija, kuri ismeta info, tos pasirinktos eilutes, atskyrame langelyje
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = str(item['values'])
        showinfo(title='Information', message=' '.join(record))
# --------- Treeview lentele pabaiga ------------ #

# komandos:
def darbuotojo_ivedimas():
    ivesta_vardas = laukas_vardas.get()
    ivesta_pavarde = laukas_pavarde.get()
    ivesta_gimtadienis = laukas_gimtadienis.get()
    ivesta_pareigos = laukas_pareigos.get()
    ivesta_atlyginimas = laukas_atlyginimas.get()
    darbuotojas = Darbuotojai(ivesta_vardas, ivesta_pavarde, ivesta_gimtadienis, ivesta_pareigos, ivesta_atlyginimas)
    session.add(darbuotojas)
    session.commit()
    atnaujinti_laukus()


def darbuotojo_redagavimas():
    pasirinktas_darbuotojas = gauti_visus_darbuotojus()[tree.selection()[0]]
    pasirinktas_id.set(pasirinktas_darbuotojas.id)
    vardas = laukas_vardas.get()
    pavarde = laukas_pavarde.get()
    gimtadienis = laukas_gimtadienis.get()
    pareigos = laukas_pareigos.get()
    atlyginimas = laukas_atlyginimas.get()
    if len(vardas) > 0:
        darbuotojas.name = vardas
    elif len(pavarde) > 0:
        darbuotojas.surname = pavarde
    elif gimtadienis:
        darbuotojas.birthday = datetime.datetime.strptime(gimtadienis, "%Y-%m-%d")
    elif len(pareigos) > 0:
        darbuotojas.position = pareigos
    elif atlyginimas:
        darbuotojas.salary = atlyginimas
    session.commit()
    
def darbuotojo_istrynimas():
    pasirinktas_darbuotojas = selectItem()['values']
    darbuotojas = session.query(Darbuotojai).get(pasirinktas_darbuotojas)
    session.delete(darbuotojas)
    session.commit()

def gauti_visus_darbuotojus():
    darbuotoju_sarasas = []
    darbuotojai = session.query(Darbuotojai).all()
    for darbuotojas in darbuotojai:
        darbuotoju_sarasas.append((darbuotojas.id, 
            darbuotojas.name, darbuotojas.surname, 
            darbuotojas.birthday, darbuotojas.position,
            darbuotojas.salary, darbuotojas.year)
        )
    for darbuotojai in darbuotoju_sarasas:
        return darbuotojai  

def atnaujinti_laukus():
    tree.delete(*tree.get_children()) #.get_children yra pythono funkcija
    tree.insert('', END, values=gauti_visus_darbuotojus())
    laukas_vardas.delete(0, END)
    laukas_pavarde.delete(0, END)
    laukas_gimtadienis.delete(0, END)
    laukas_pareigos.delete(0, END)
    laukas_atlyginimas.delete(0, END)

def selectItem():
    curItem = tree.focus()
    return tree.item(curItem)

# uzrasai
uzrasas_tuscias = Label(langas, text='')
uzrasas_ivesti = Label(langas, text="Įveskite darbuotoją:")
uzrasas_vardas = Label(langas, text="Vardas: ")
uzrasas_pavarde = Label(langas, text="Pavardė: ")
uzrasas_gimtadienis = Label(langas, text="Gimimo data: ")
uzrasas_pareigos = Label(langas, text="Pareigos: ")
uzrasas_atlyginimas = Label(langas, text="Atlyginimas: ")
uzrasas_redaguoti = Label(langas, text="Redaguoti darbuotoją:")
uzrasas_tuscias1 = Label(langas, text='')

# laukai ivedimui
laukas_vardas = Entry(langas)
laukas_pavarde = Entry(langas)
laukas_gimtadienis = Entry(langas)
laukas_pareigos = Entry(langas)
laukas_atlyginimas = Entry(langas)

# mygtukai
mygtukas_irasymo = Button(langas, text="Įrašyti", command=darbuotojo_ivedimas)
langas.bind("<Return>", lambda event: darbuotojo_ivedimas())
mygtukas_trinimui = Button(langas, text="Ištrinti", command=darbuotojo_istrynimas)
mygtukas_redaguoti = Button(langas, text="Redaguoti", command=darbuotojo_redagavimas)

# grid'ai label'ams
uzrasas_tuscias.grid(row=0, column=0, sticky=W)
uzrasas_ivesti.grid(row=1, column=1, sticky=W)
uzrasas_vardas.grid(row=2, column=1, sticky=W)
uzrasas_pavarde.grid(row=3, column=1, sticky=W)
uzrasas_gimtadienis.grid(row=4, column=1, sticky=W)
uzrasas_pareigos.grid(row=5, column=1, sticky=W)
uzrasas_atlyginimas.grid(row=6, column=1, sticky=W)
uzrasas_tuscias1.grid(row=7, column=0, sticky=W)

# gridai Entry'iems
laukas_vardas.grid(row=2, column=2)
laukas_pavarde.grid(row=3, column=2)
laukas_gimtadienis.grid(row=4, column=2)
laukas_pareigos.grid(row=5, column=2)
laukas_atlyginimas.grid(row=6, column=2)

# gridai Button'ams
mygtukas_irasymo.grid(row=3, column=3, ipadx=50)
mygtukas_redaguoti.grid(row=4, column=3, ipadx=40)
mygtukas_trinimui.grid(row=5, column=3, ipadx=50)

# treeview
# tree.bind('<<TreeviewSelect>>')
tree.grid(row=9, column=1, columnspan=13, sticky='nsew')
scrollbar = ttk.Scrollbar(langas, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=9, column=14, sticky='ns')

# lango paleidimas
langas.mainloop()
