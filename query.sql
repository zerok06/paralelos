CREATE DATABASE IF NOT EXISTS escuela;

CREATE TABLE IF NOT EXISTS alumno (
    carnet INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    nota DECIMAL(4, 2) NOT NULL
);

INSERT INTO
    alumno (nombres, apellidos, nota)
VALUES
    ("Javier", "Fernández", 12.00),
    ("Carlos", "Villanueva", 12.00),
    ("José", "Paye", 12.00),
    ("Ricardo", "Mamani", 12.00),
    ("Alex", "Quispe", 12.00),
    ("Juana", "Valera", 12.00);