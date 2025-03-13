#!/bin/bash

# Verificar si el archivo de base de datos existe
if [ ! -f laboratorio.db ]; then
    echo "La base de datos no existe. Creando la base de datos..."
    # Crear la base de datos e inicializarla con el archivo initdb.sql
    sqlite3 laboratorio.db < initdb.sql
else
    echo "La base de datos ya existe."
fi

echo "Selecciona una acción:"
echo "1. Agregar paciente"
echo "2. Ver pacientes"
echo "3. Agregar medición EEG"
echo "4. Ver mediciones de un paciente"
echo "5. Eliminar medición EEG"

read accion

if [ $accion = "1" ]; then
    echo "Ingrese el nombre del paciente:"
    read nombre
    echo "Ingrese la edad del paciente:"
    read edad
    sqlite3 laboratorio.db "INSERT INTO pacientes (nombre, edad) VALUES ('$nombre', $edad)"
elif [ $accion = "2" ]; then
    echo "Lista de pacientes:"
    sqlite3 laboratorio.db "SELECT * FROM pacientes"
elif [ $accion = "3" ]; then
    echo "Ingrese el ID del paciente para agregar medición EEG:"
    read paciente_id
    echo "Ingrese la medición delta:"
    read delta
    echo "Ingrese la medición theta:"
    read theta
    echo "Ingrese la medición alpha:"
    read alpha
    echo "Ingrese la medición beta:"
    read beta
    echo "Ingrese la medición gamma:"
    read gamma
    echo "Ingrese la amplitud:"
    read amplitud
    echo "Ingrese notas (opcional):"
    read notas
    echo "Ingrese la fecha (YYYY-MM-DD HH:MM:SS):"
    read fecha
    sqlite3 laboratorio.db "INSERT INTO mediciones (paciente_id, delta, theta, alpha, beta, gamma, amplitud, notas, fecha) VALUES ($paciente_id, $delta, $theta, $alpha, $beta, $gamma, $amplitud, '$notas', '$fecha')"
elif [ $accion = "4" ]; then
    echo "Ingrese el ID del paciente para ver las mediciones EEG:"
    read paciente_id
    echo "Mediciones EEG del paciente con ID $paciente_id:"
    sqlite3 laboratorio.db "SELECT * FROM mediciones WHERE paciente_id = $paciente_id"
elif [ $accion = "5" ]; then
    echo "Ingrese el ID de la medición EEG a eliminar:"
    read medicion_id
    sqlite3 laboratorio.db "DELETE FROM mediciones WHERE id = $medicion_id"
    echo "Medición eliminada."
else
    echo "Acción no válida."
fi
