Ejemplo: Base de datos de empleados y departamentos
Vamos a crear dos tablas: una tabla para departamentos y otra para empleados. Los empleados estarán asociados a un departamento, lo que implica que la tabla de empleados tendrá una clave foránea que se refiere a la tabla de departamentos.

Paso 1: Crear la tabla de departamentos
Primero, vamos a crear una tabla para los departamentos. La columna id será la clave primaria.

sql
Copiar
CREATE TABLE departamentos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);
Paso 2: Crear la tabla de empleados con una clave foránea
La tabla de empleados tendrá una columna departamento_id que será una clave foránea que hace referencia a la columna id en la tabla departamentos.

sql
Copiar
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    departamento_id INTEGER,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);
En este caso, la columna departamento_id en la tabla empleados es una clave foránea que hace referencia al campo id de la tabla departamentos.

Paso 3: Insertar datos
Ahora podemos insertar algunos datos en ambas tablas.

Insertar algunos departamentos:
sql
Copiar
INSERT INTO departamentos (nombre) VALUES ('Recursos Humanos');
INSERT INTO departamentos (nombre) VALUES ('Desarrollo');
INSERT INTO departamentos (nombre) VALUES ('Marketing');
Insertar algunos empleados:
sql
Copiar
INSERT INTO empleados (nombre, departamento_id) VALUES ('Juan Pérez', 1);  -- Juan Pérez trabaja en Recursos Humanos
INSERT INTO empleados (nombre, departamento_id) VALUES ('Ana Gómez', 2);   -- Ana Gómez trabaja en Desarrollo
INSERT INTO empleados (nombre, departamento_id) VALUES ('Carlos López', 3);  -- Carlos López trabaja en Marketing
Paso 4: Consultar los datos
Finalmente, puedes hacer una consulta para ver cómo los empleados están asociados con los departamentos.

sql
Copiar
SELECT empleados.nombre AS empleado, departamentos.nombre AS departamento
FROM empleados
JOIN departamentos ON empleados.departamento_id = departamentos.id;
Este es el resultado que obtendrás:

diff
Copiar
empleado        | departamento
----------------|--------------
Juan Pérez      | Recursos Humanos
Ana Gómez       | Desarrollo
Carlos López    | Marketing
Paso 5: Activar el soporte de claves foráneas
SQLite, por defecto, no tiene habilitado el soporte de claves foráneas, por lo que es necesario habilitarlo para que la integridad referencial funcione correctamente.

Para habilitar las claves foráneas en SQLite3, ejecuta el siguiente comando después de abrir tu base de datos:

sql
Copiar
PRAGMA foreign_keys = ON;