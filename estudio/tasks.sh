sqlite3 tareas.db < initdb.sql

echo "Selecciona una accion"
echo "1. Agregar tarea"
echo "2. Ver tareas"
echo "3. Marcar tarea como completada"

read accion

if [ $accion = "1" ]
then
    echo "Ingrese la tarea"
    read tarea
    echo "Ingrese una descripción (opcional)"
    read descripcion
    sqlite3 tareas.db "insert into tasks (title, description) values ('$tarea', '$descripcion')"
elif [ $accion = "2" ]
then
    sqlite3 tareas.db "select * from tasks"
elif [ $accion = "3" ]
then
    sqlite3 tareas.db "select * from tasks where status = 'pending'"
    echo "Ingrese el id de la tarea que desea marcar como completada"
    read id
    sqlite3 tareas.db "update tasks set status = 'completed' where id = $id"
fi