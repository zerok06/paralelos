from mysql import connector
import threading
from prettytable import from_db_cursor, PrettyTable
import os


DB_QUERY = connector.connect(
    host="localhost", user="root", password="", database="escuela"
)

clear = lambda: os.system("cls")


def ordenar_por_nota(estudiantes):
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if estudiantes[j][3] > estudiantes[j + 1][3]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
    return estudiantes


def ordenar_por_nombres(estudiantes):
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if estudiantes[j][1] > estudiantes[j + 1][1]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
    return estudiantes


def ordenar_por_carnet(estudiantes):
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if estudiantes[j][0] > estudiantes[j + 1][0]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
    return estudiantes


def option1():
    execute = DB_QUERY.cursor()
    query = "INSERT INTO alumno(nombres,apellidos,nota) VALUES (%s,%s,%s)"
    valores = [
        ("Javier", "Fernández", 12.00),
        ("Carlos", "Villanueva", 12.00),
        ("José", "Paye", 12.00),
        ("Ricardo", "Mamani", 12.00),
        ("Alex", "Quispe", 12.00),
        ("Juana", "Valera", 12.00),
    ]
    execute.executemany(query, valores)
    print("Alumnos registrados...")


def option2():
    execute = DB_QUERY.cursor()
    query = "INSERT INTO alumno(nombres,apellidos,nota) VALUES (%s,%s,%s)"
    nombres = str(input("Nombre de alumno:"))
    apellidos = str(input("Apellido de alumno:"))
    nota = float(input("Nota de alumno:"))
    execute.execute(query, (nombres, apellidos, nota))
    print("Alumno registrado...")


def option3():
    execute = DB_QUERY.cursor()
    execute.execute("SELECT * FROM alumno")
    rows = execute.fetchall()
    if execute.rowcount > 0:
        execute.execute("SELECT * FROM alumno")
        printRows = from_db_cursor(execute)
        print("\n")
        print(printRows)
        print("\n")

    else:
        print("Lista vacía...")


def option4():
    execute = DB_QUERY.cursor()
    execute.execute("SELECT * FROM alumno")
    rows = execute.fetchall()
    if execute.rowcount > 0:
        ordenada = ordenar_por_nota(rows)
        table = PrettyTable(["Carnet", "Nombres", "Apellidos", "Nota"])
        table.add_rows(ordenada)
        print("\n")
        print(table)
        print("\n")

    else:
        print("Lista vacía...")


def option5():
    execute = DB_QUERY.cursor()
    execute.execute("SELECT * FROM alumno")
    rows = execute.fetchall()
    if execute.rowcount > 0:
        ordenada = ordenar_por_nombres(rows)
        table = PrettyTable(["Carnet", "Nombres", "Apellidos", "Nota"])
        table.add_rows(ordenada)
        print("\n")
        print(table)
        print("\n")

    else:
        print("Lista vacía...")


def option6():
    execute = DB_QUERY.cursor()
    execute.execute("SELECT * FROM alumno")
    rows = execute.fetchall()
    if execute.rowcount > 0:
        ordenada = ordenar_por_carnet(rows)
        table = PrettyTable(["Carnet", "Nombres", "Apellidos", "Nota"])
        table.add_rows(ordenada)
        print("\n")
        print(table)
        print("\n")

    else:
        print("Lista vacía...")


options = {
    "1": option1,
    "2": option2,
    "3": option3,
    "4": option4,
    "5": option5,
    "6": option6,
}


def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    while True:
        print("1. Cargar Automáticamente de Datos")
        print("2. Registrar Alumno")
        print("3. Consultar General")
        print("4. Ordenar por Nota")
        print("5. Ordenar Alfabéticamente")
        print("6. Ordenar por carnet")
        print("7. Exit")
        choice = input("Ingresa un opción: ")
        clear()
        if choice in options:
            t = threading.Thread(target=options[choice])
            t.start()
            t.join()
        elif choice == "7":
            break
        else:
            print("Intenta de nuevo.")


main()
