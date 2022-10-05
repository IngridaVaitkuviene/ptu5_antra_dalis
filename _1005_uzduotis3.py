# Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių, 
# kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas. 
# Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. 
# Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir 
# atspausdinus paskutinį, parašytų 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu. 
# Sugalvokite, kaip apeiti šią problemą (hint - type conversion, if sąlygos).

# tarkim, kad teisingas pin kodas yra 0649
PIN = "0649"

def pin_breaker():
    spejimas = 0
    while True:
        yield spejimas
        if spejimas == int(PIN):
            if len(str(PIN)) < 4:
                if len(str(spejimas)) == 3:
                    print(f"PIN is 0{spejimas}!")
                elif len(str(spejimas)) == 2:
                    print(f"PIN is 00{spejimas}!")
                else:
                    print(f"PIN is 000{spejimas}!")
            else:
                print(f"PIN is 0{spejimas}")
            break
        spejimas += 1

generator = pin_breaker()
for number in generator:
    print(f"0{number}")