# Parašykite generatorų , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių. 
# (Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233. 
# Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:)

def fibonachi():
    a, b = 0, 1 # a = 0, b = 1
    while True:
        yield a
        (a, b) = (b, a+b) # a = b, b = a+b, cia yra tuples

fibai = fibonachi()

counter = 0
while True:
    print(counter, next(fibai))
    c = input("Enter for next number, 'x/q' to quit: ")
    if c.casefold() == "x" or c.casefold() == "q":
        break
    counter += 1
