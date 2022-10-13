-- Platesnis WHERE panaudojimas, BETWEEN ... AND ...., veikia ne tik grupevime, bet ir where salygoje
SELECT * FROM cars WHERE price BETWEEN 10000 AND 30000;
-- galima tikrinti ir pagal sąrašą
SELECT * FROM cars WHERE year in (2005, 2010, 2011) ORDER BY year;
-- paieška tekste. make stulpelyje ieskome teksto su Like kur modeliai prasideda su t raide % - reiškia nulį arba keletą simbolių 
SELECT * FROM cars WHERE make LIKE "T%";
SELECT * FROM cars WHERE make LIKE "%a";
SELECT * FROM cars WHERE make LIKE "%t%";
-- placeholderis vieno simbolio koziris "_". _ - reiškia vieną simbolį
SELECT * FROM cars WHERE model LIKE "__";
SELECT * FROM cars WHERE model LIKE "X_";
SELECT * FROM cars WHERE model LIKE "X%";
SELECT * FROM cars WHERE make LIKE "__n%";
-- NULL
SELECT * FROM cars WHERE color IS NULL;
UPDATE cars SET color="Ugly" WHERE color is NULL;
SELECT * FROM cars WHERE color LIKE "Ugly";
-- Loginės sąlygos AND, OR, NOT
SELECT * FROM cars WHERE make = "Ford" AND price > 40000;
SELECT * FROM cars WHERE price < 40000 OR color = "Pink";
SELECT * FROM cars WHERE (price < 40000 OR color = "Pink") AND year > 2000;
SELECT * FROM cars WHERE color NOT IN ("Violet", "Pink", "Yellow", "Turquoise", "Ugly", "Fuscia");
SELECT * FROM cars WHERE (make = "Volvo" OR make = "Ford") AND price NOT BETWEEN 10000 AND 50000;
-- pirma lygybe, tada not, tada and ir tada or
-- Rūšiavimas
SELECT * FROM cars ORDER BY year;
SELECT * FROM cars ORDER BY year DESC LIMIT 5;
-- kaip pasižiūrėti sekančius 5-is;
SELECT * FROM cars ORDER BY year DESC LIMIT 5 OFFSET 5;
-- išrūšiuoja pagal abėcėlę
SELECT * FROM cars ORDER BY make;
-- nekreipti dėmesio į raidžių dydį
SELECT * FROM cars WHERE make="TOYOTA" COLLATE NOCASE;
-- rezultatų manipuliavimas su || operatorium
SELECT "Gamintojas: " || make AS gamintojas, model AS modelis FROM cars LIMIT 10;
-- Skaičiavimai
SELECT make, model, price, round(price/3.4528, 2) AS price_euro FROM cars;
SELECT make || " " || model || ", " || year as car_model_year FROM cars ORDER BY year;
-- amžiaus skaičiavimas
SELECT make, model, 2022 - year AS age FROM cars ORDER BY age;
SELECT make, model, price, round(price/1.18) as "price ex vat" FROM cars ORDER BY "price ex vat";
-- TEISINGAS grupavimas
-- avg() - vidurkis
-- min() ir max()
-- count() - skaičiuoja
-- sum() - sumuoja
SELECT sum(price) FROM cars;
SELECT make, sum(price) FROM cars GROUP BY make;
SELECT avg(year) FROM cars;
SELECT avg(year) FROM cars GROUP BY make;
-- Darant kompleksiškas užklausas, reikėtų laikytis tokio eiliškumo:
-- SELECT stulpelis, grupinė_funkcija
-- FROM lentelė
-- WHERE sąlyga]
-- [GROUP BY sąrašas_grupavimui]
-- [HAVING grupės sąlyga]
-- [ORDER BY rūšiavimo sąlyga]
SELECT make, avg(year), count(*) FROM cars GROUP BY make HAVING count(*) > 1;
SELECT make, avg(price), count(*) FROM cars GROUP BY make HAVING count(*) > 1;
SELECT min(price), max(price), avg(price) FROM cars;
SELECT max(price), make, model FROM cars;
SELECT color, max(price), avg(price), min(price), make, model, count(*) FROM cars GROUP BY color ORDER BY price DESC;
SELECT color, avg(price), avg(price), min(price), make, model, count(*) FROM cars GROUP BY color ORDER BY price DESC;
SELECT color, round(avg(price), 2), make, model, count(*) FROM cars GROUP BY color ORDER BY price DESC;

--SELECT make, model, year, price
--FROM cars
--WHERE make NOT IN ("Toyota", "Mercury", "Volvo")
--GROUP BY price
--HAVING year > 2007
--ORDER BY make;
-- susirinkom duomenis 
SELECT make, model, year, max(price), color, count(*)
-- is cars lenteles
FROM cars
-- kurios ne toyota mercury ir volvo, filtruojam duomenis, kuriuos grupuosim, tada iskelsim salyga ir surusiuosim
WHERE make NOT IN ("Toyota", "Mercury", "Volvo")
-- grupuojam pagl metus, 
GROUP BY year
-- itraukiam salyga, kad spalva nebutu pink ir turkiska ir kad daugiau butu uz viena, salyga grupavimui
HAVING color NOT IN ("Pink", "Turquoise") AND count(*) > 1
-- ir rusiuojam pagal metus
ORDER BY year;






