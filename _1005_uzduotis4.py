# Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą, 
# ir grąžintų po vieną eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). 
# Reikės prisiminti darbą su failais :)

def read_in_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            yield line[:-1]


generator = read_in_lines('tekstas/tekstas.txt')

for x in generator:
    print(x)

