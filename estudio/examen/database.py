import sqlite3

DB_NAME = "laboratorio.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def agregar_paciente(nombre, edad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pacientes (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()

def agregar_medicion(paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas=""):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO mediciones (paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas)
    )
    conn.commit()
    conn.close()

def obtener_mediciones_paciente(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.*
        FROM mediciones m
        JOIN pacientes p ON m.paciente_id = p.id
        WHERE p.nombre = ?
    """, (nombre,))
    datos = cursor.fetchall()
    conn.close()
    return datos

def obtener_mediciones_frecuencia(nombre, frecuencia):
    if frecuencia not in ["delta", "theta", "alpha", "beta", "gamma"]:
        return None

    conn = conectar()
    cursor = conn.cursor()
    query = f"""
        SELECT m.{frecuencia}
        FROM mediciones m
        JOIN pacientes p ON m.paciente_id = p.id
        WHERE p.nombre = ?
    """
    cursor.execute(query, (nombre,))
    datos = cursor.fetchall()
    conn.close()
    return datos

def obtener_mediciones_amplitud(nombre, amplitud_min, amplitud_max):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.*
        FROM mediciones m
        JOIN pacientes p ON m.paciente_id = p.id
        WHERE p.nombre = ? AND m.amplitud BETWEEN ? AND ?
    """, (nombre, amplitud_min, amplitud_max))
    datos = cursor.fetchall()
    conn.close()
    return datos

def eliminar_medicion(id_medicion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mediciones WHERE id = ?", (id_medicion,))
    conn.commit()
    conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    agregar_paciente("Juan Pérez", 30)
    agregar_medicion(1, 3.2, 5.1, 10.5, 20.3, 40.8, 95.5, "Medición inicial")
    print(obtener_mediciones_paciente("Juan Pérez"))
