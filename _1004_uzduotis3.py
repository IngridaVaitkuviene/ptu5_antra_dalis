# Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti. 
# Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais vykdymo laikas - XX s. 
# Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija, išrenkančia pirminius skaičius užduotame diapazone.
# Turime tokį kodą:

from functools import wraps
# importuojame requests
import requests
# importuojame time modulį  
from time import time
 
# pasirasom dekoratoriu bet kokios funkcijos vykdymo laikui fiksuoti
def speed_test(funkcija):
    @wraps(funkcija)
    def wrapper(*args, **kwargs):
        # fiksuojame starto laiką
        start_time = time()
        funkcija(*args, **kwargs)
        # fiksuojame pabaigos laiką 
        end_time = time()
        runtime = end_time - start_time
        # atspausdiname laiką, per kurį gavome atsakymą 
        print(f"Function's '{funkcija.__name__}', with given parameters {args} runtime: {round(runtime, 2)}s")
    return wrapper

@speed_test
def get_status(website):
    # sukuriame http užklausą r = requests.get('http://www.cnn.com')
    r = requests.get(website)
    # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes) 
    print(r.status_code)

get_status('http://python.org')

@speed_test
def prime_finder(given_range):
    final_list = []
    for number in range(given_range):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                final_list.append(number)
    return final_list

prime_finder(10000)