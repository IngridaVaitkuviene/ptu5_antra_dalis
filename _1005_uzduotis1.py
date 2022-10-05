# Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next() grąžintų sekantį porinį skaičių. 
# Pirmas sk. 2, toliau 4 ir taip be pabaigos.

def skaiciuojam_porinius():
    skaicius = 2
    while True:
        yield skaicius
        skaicius += 2

poriniai = skaiciuojam_porinius()

while True:
    print(next(poriniai))