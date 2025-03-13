-- Crear la tabla de pacientes
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
);

-- Crear la tabla de mediciones EEG
CREATE TABLE mediciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    delta REAL,
    theta REAL,
    alpha REAL,
    beta REAL,
    gamma REAL,
    amplitud REAL,
    notas TEXT,
    fecha TEXT,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
);
