-- CREATE TABLE
-- VARCHAR VariousCharacters
CREATE TABLE coder (
	First_name VARCHAR(50),
	last_name VARCHAR(100),
	email VARCHAR(255),
	age INTEGER,
	xp_years INTEGER
);
-- Sukūrėme lentelę coder, kurioje stulpeliai vardas, pavardė, amžius, patirtis(metais) turi nurodytus duomenų tipus.
-- jei blogai nurodem stulpelio pavadinima, pataisyti taip:
--ALTER TABLE coders RENAME "email" TO "e-mail";

-- Sukūriam antrą lentelę:
CREATE TABLE coders (
	id PRIMARY KEY NOT NULL AUTOINCREMENT,
	first_name VARCHAR(50),
	last_name VARCHAR(100),
	email VARCHAR(255),
	age INTEGER,
	age INTEGER CHECK (age > 17 AND age < 75),
	xp_years INTEGER CHECK (xp_years > 0 AND xp_years < 50)
	
);