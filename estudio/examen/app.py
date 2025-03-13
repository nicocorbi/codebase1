import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("laboratorio.db")
c = conn.cursor()

# Crear las tablas a partir del archivo initdb.sql
def create_table():
    with open("initdb.sql", "r") as f:
        c.executescript(f.read())
    conn.commit()

# Función para agregar un paciente
def add_patient(nombre, edad):
    c.execute("INSERT INTO pacientes (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()

# Función para agregar una medición de EEG
def add_medicion(paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas, fecha):
    c.execute("""
    INSERT INTO mediciones (paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas, fecha)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas, fecha))
    conn.commit()

# Función para obtener todas las mediciones de un paciente
def get_mediciones_by_patient(paciente_id):
    c.execute("""
    SELECT * FROM mediciones WHERE paciente_id = ?
    """, (paciente_id,))
    return c.fetchall()

# Función para obtener mediciones de un paciente por frecuencia
def get_mediciones_by_frequency(paciente_id, frecuencia):
    c.execute(f"""
    SELECT * FROM mediciones WHERE paciente_id = ? AND {frecuencia} IS NOT NULL
    """, (paciente_id,))
    return c.fetchall()

# Función para obtener mediciones de un paciente por amplitud
def get_mediciones_by_amplitud(paciente_id, amplitud):
    c.execute("""
    SELECT * FROM mediciones WHERE paciente_id = ? AND amplitud = ?
    """, (paciente_id, amplitud))
    return c.fetchall()

# Función para eliminar una medición
def delete_medicion(medicion_id):
    c.execute("""
    DELETE FROM mediciones WHERE id = ?
    """, (medicion_id,))
    conn.commit()

# Llamar a la función para crear las tablas (si aún no existen)
create_table()

# Ejemplo de agregar un paciente
add_patient("Juan Pérez", 30)

# Ejemplo de agregar mediciones EEG para el paciente con ID 1
add_medicion(1, 2.5, 6.0, 10.5, 20.3, 35.0, 85.0, "Medición inicial", "2025-03-13 10:00:00")

# Obtener todas las mediciones de un paciente (ID 1)
mediciones = get_mediciones_by_patient(1)
print(mediciones)

# Obtener mediciones de un paciente (ID 1) para una frecuencia específica (ejemplo: 'delta')
mediciones_delta = get_mediciones_by_frequency(1, 'delta')
print(mediciones_delta)

# Obtener mediciones de un paciente (ID 1) para una amplitud específica (ejemplo: 85.0)
mediciones_amplitud = get_mediciones_by_amplitud(1, 85.0)
print(mediciones_amplitud)

# Eliminar una medición por su ID (ejemplo: eliminar medición con ID 1)
delete_medicion(1)

# Cerrar la conexión
conn.close()

