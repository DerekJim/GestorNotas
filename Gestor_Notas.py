#Alumno: Derek Stuard Jimenez Deleón
#Carnet: 7590-25-10502
#Sección: B
#Actualizacion: 05/09/2025

# Gestor de Notas Académicas
from collections import deque

#Menu principal del gestor de notas y sus opciones
def mostrar_menu():
    print("=== GESTOR DE NOTAS ACADEMICAS ===")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por código (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión de notas")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    print("Seleccione una opción (1-13): ", end='')

#Esta es la función principal que ejecuta el menú y llama a las funciones correspondientes
def main():
    while True:
        mostrar_menu()
        opcion = input()
        if opcion == '1':
            registrar_curso()
        elif opcion == '2':
            mostrar_cursos()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            contar_aprobados_reprobados()
        elif opcion == '5':
            buscar_curso_lineal()
        elif opcion == '6':
            actualizar_nota()
        elif opcion == '7':
            eliminar_curso()
        elif opcion == '8':
            ordenar_por_nota()
        elif opcion == '9':
            ordenar_por_nombre()
        elif opcion == '10':
            buscar_curso_binaria()
        elif opcion == '11':
            simular_cola_revisiones()
        elif opcion == '12':
            mostrar_historial_cambios()
        elif opcion == '13':
            print("Saliendo del gestor de notas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 13.")

# Lista de cursos 
cursos = []
# Pila para historial de cambios
historial_cambios = []
# Cola para solicitudes de revisión
cola_revisiones = deque()

# Esta funcion registra un nuevo curso y permite ingresar su nota
def registrar_curso():
    codigo = input("Ingrese el código del curso (ej. 008): ")

    # Permite verificar si el código ya existe y que no se duplique
    for curso in cursos:
        if curso['codigo'] == codigo:
            print(f"Ya existe un curso con el código {codigo}. No se puede registrar duplicados.")
            return
    nombre = input("Ingrese el nombre del curso: ")
    try:
        nota = int(input("Ingrese la nota del curso: "))
        if nota < 0 or nota > 100:
            print("Nota inválida. Debe estar entre 0 y 100.")
            return
    except ValueError:
        print("Entrada inválida. La nota debe ser un número.")
        return
    
    print("---------------------------------------------")
    curso = {'codigo': codigo, 'nombre': nombre, 'nota': nota}
    cursos.append(curso)
    historial_cambios.append(f"Se registró el curso {codigo} '{nombre}' con nota {nota}.")
    print(f"Curso {codigo} '{nombre}' con nota {nota} registrado exitosamente.")
    print("---------------------------------------------")

# Esta funcion permite mostrar los cursos y sus notas
def mostrar_cursos():
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("Cursos y notas registrados:")
        for curso in cursos:
            print(f"Código: {curso['codigo']}, Curso: {curso['nombre']}, Nota: {curso['nota']}")
    print("---------------------------------------------")

# Esta funcion permite calcular el promedio general de las notas
def calcular_promedio():
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados para calcular el promedio.")
    else:
        total_notas = sum(curso['nota'] for curso in cursos)
        promedio = total_notas / len(cursos)
        print(f"El promedio general de las notas es: {promedio:.2f}")
    print("---------------------------------------------")

#Esta funcion permite contar los cursos que fueron aprobados/reprobados
def contar_aprobados_reprobados():
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados para contar aprobados y reprobados.")
    else:
        aprobados = sum(1 for curso in cursos if curso['nota'] >= 60)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}, Cursos reprobados: {reprobados}")
    print("---------------------------------------------")

# Esta funcion permite buscar un curso por su nombre usando búsqueda lineal
def buscar_curso_lineal():
    print("---------------------------------------------")
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ")
    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscar.lower():
            print(f"Curso encontrado: {curso['codigo']} - {curso['nombre']}, Nota: {curso['nota']}")
            print("---------------------------------------------")
            return
    print("Curso no encontrado.")
    print("---------------------------------------------")

# Esta funcion permite actualizar la nota de un curso existente 
def actualizar_nota():
    print("---------------------------------------------")
    codigo_actualizar = input("Ingrese el código del curso a actualizar: ")
    for curso in cursos:
        if curso['codigo'] == codigo_actualizar:
            try:
                nueva_nota = int(input(f"Ingrese la nueva nota para '{curso['nombre']}': "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("Nota inválida. Debe estar entre 0 y 100.")
                    print("---------------------------------------------")
                    return
                anterior = curso['nota']
                curso['nota'] = nueva_nota
                historial_cambios.append(
                    f"Se actualizó {curso['codigo']} '{curso['nombre']}' de nota {anterior} a {nueva_nota}."
                )
                print(f"Nota del curso {curso['codigo']} '{curso['nombre']}' actualizada a {nueva_nota}.")
                print("---------------------------------------------")
                return
            except ValueError:
                print("Entrada inválida. La nota debe ser un número.")
                print("---------------------------------------------")
                return
    print("Curso no encontrado.")
    print("---------------------------------------------")

# Esta funcion permite eliminar un curso por su código y registra el cambio en el historial
def eliminar_curso():
    print("---------------------------------------------")
    codigo_eliminar = input("Ingrese el código del curso a eliminar: ")
    for i, curso in enumerate(cursos):
        if curso['codigo'] == codigo_eliminar:
            eliminado = cursos.pop(i)
            historial_cambios.append(
                f"Se eliminó el curso {eliminado['codigo']} '{eliminado['nombre']}' con nota {eliminado['nota']}."
            )
            print(f"Curso {codigo_eliminar} eliminado exitosamente.")
            print("---------------------------------------------")
            return
    print("Curso no encontrado.")
    print("---------------------------------------------")

# Está función ordena los cursos por nota usando el método de burbuja 
# Esta funcion fue investigada en: https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/
# fuentes adicionales : https://youtu.be/TeerSd_ZqJQ?feature=shared
def ordenar_por_nota():
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados para ordenar.")
    else:
        n = len(cursos)
        for i in range(n):
            for j in range(0, n-i-1):
                if cursos[j]['nota'] > cursos[j+1]['nota']:
                    cursos[j], cursos[j+1] = cursos[j+1], cursos[j]
        print("Cursos ordenados por nota (de menor a mayor):")
        mostrar_cursos()
    print("---------------------------------------------")  

# Esta función ordena los cursos por nombre usando el método de inserción 
# Esta funcion fue investigada en: https://youtu.be/6GU6AGEWYJY?feature=shared
# La idea de la funcion fue tomada del video y adaptada al contexto del gestor de notas
def ordenar_por_nombre():   
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados para ordenar.")
    else:
        for i in range(1, len(cursos)):
            key = cursos[i]
            j = i-1
            while j >= 0 and key['nombre'].lower() < cursos[j]['nombre'].lower():
                cursos[j + 1] = cursos[j]
                j -= 1
            cursos[j + 1] = key
        print("Cursos ordenados por nombre (alfabéticamente):")
        mostrar_cursos()
    print("---------------------------------------------")

# Función de búsqueda binaria para encontrar un curso por su código
def buscar_curso_binaria():
    print("---------------------------------------------")
    if not cursos:
        print("No hay cursos registrados para buscar.")
        print("---------------------------------------------")
        return
    
    # ordenar por código antes de buscar usando búsqueda binaria
    # Esta parte del codigp indica que se ordene la lista de cursos por su código antes de realizar la búsqueda binaria
    # Esto es necesario porque la búsqueda binaria solo funciona en listas ordenadas
    cursos.sort(key=lambda x: x['codigo'])  
    
    codigo_buscar = input("Ingrese el código del curso a buscar (ej. 008): ")
    izquierda, derecha = 0, len(cursos) - 1             
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if cursos[medio]['codigo'] == codigo_buscar:
            print(f"Curso encontrado: {cursos[medio]['codigo']} - {cursos[medio]['nombre']}, Nota: {cursos[medio]['nota']}")
            print("---------------------------------------------")
            return
        elif cursos[medio]['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Curso no encontrado.")   
    print("---------------------------------------------")  

# Esta función simula una cola para gestionar solicitudes de revisión de notas
def simular_cola_revisiones():
    print("---------------------------------------------")
    while True:
        print("\n=== Cola de Solicitudes de Revisión de Notas ===")
        print("1. Agregar solicitud")
        print("2. Procesar solicitud")
        print("3. Mostrar solicitudes en cola")
        print("4. Salir de la simulación de cola")
        opcion_cola = input("Seleccione una opción (1-4): ")
        if opcion_cola == '1':
            codigo_solicitante = input("Ingrese el código del curso para la solicitud de revisión: ")
            cola_revisiones.append(codigo_solicitante)
            print(f"Solicitud para el curso '{codigo_solicitante}' agregada a la cola.")
        elif opcion_cola == '2':
            if cola_revisiones:
                procesado = cola_revisiones.popleft()
                print(f"Procesando solicitud para el curso '{procesado}'.")
            else:
                print("No hay solicitudes en la cola.")
        elif opcion_cola == '3':
            if cola_revisiones:
                print("Solicitudes en la cola:")
                for solicitud in cola_revisiones:
                    print(f"- {solicitud}")
            else:
                print("No hay solicitudes en la cola.")
        elif opcion_cola == '4':
            print("Saliendo de la simulación de cola.")
            print("---------------------------------------------")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.") 
    print("---------------------------------------------")

# Esta funcion permite mostrar el historial de cambios realizados en los cursos
# La función utiliza una pila (lista) para almacenar los cambios y los muestra en orden inverso (último en entrar, primero en salir)
def mostrar_historial_cambios():
    print("---------------------------------------------")  
    if not historial_cambios:
        print("No hay cambios en el historial.")
    else:
        print("Historial de cambios (último en entrar, primero en salir):")
        for cambio in reversed(historial_cambios):
            print(f"- {cambio}")
    print("---------------------------------------------")

if __name__ == "__main__":
    main()
