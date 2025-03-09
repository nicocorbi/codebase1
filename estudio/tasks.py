import sqlite3

conn = sqlite3.connect('tareas.db')
c = conn.cursor()
# un cursor es un objeto que permite interactuar con la base de datos
# nos permite ejecutar comandos SQL

def create_table():
    #executa initdb.sql
    with open('initdb.sql', 'r') as f: # r La 'r' es el modo de apertura del archivo. En este caso, 'r' significa "read" (lectura)
        c.executescript(f.read()) #La f es simplemente una variable que hace referencia al archivo que se ha abierto. Dentro del bloque with, se puede usar f para interactuar con el archivo.
                                    #En este caso, se utiliza para leer el contenido del archivo con f.read(), lo que devuelve todo el texto contenido en initdb.sql.
    conn.commit()

def add_task(task, description=None):
    c.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (task, description))
    conn.commit()

def get_tasks():
    c.execute('SELECT * FROM tasks')
    return c.fetchall()# devuelve todas las filas del conjunto de resultados de una consulta SQL como una lista de tuplas.

def complete_task(task_id):
    c.execute('UPDATE tasks SET status = "completed" WHERE id = ?', (task_id,))
    conn.commit()

def complete_task_by_title(title):
    c.execute('UPDATE tasks SET status = "completed" WHERE title = ?', (title,))
    conn.commit()

def delete_task(task_id):
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()

while True:
    print('1. Add task')
    print('2. List tasks')
    print('3. Complete task')
    print('4. Delete task')
    print('5. Exit')

    option = input('Choose an option: ')
    
    if option == '1':
        task = input('Enter the task: ')
        desc = input('Enter the description: (optional)')
        add_task(task, desc)

    elif option == '2': #elif es una forma de agregar una condición adicional a una estructura if-else en Python.
#En el caso del código proporcionado, se ejecuta un bloque de código si option es igual a '2', lo que significa que se recuperan y muestran las tareas.
        tasks = get_tasks()
        print('ID | Task | Description | Status')
        for task in tasks:
            line= f'{task[0]} | {task[1]} | {task[2]} | {task[3]}'
            print(line) # line es una variable que almacena una cadena de texto (string)

    elif option == '3':
        task_id = input('Enter the task id: ')
        complete_task(task_id)

    elif option == '4':
        task_id = input('Enter the task id: ')
        delete_task(task_id)

    elif option == '5':
        break
        