#Alumno: Derek Stuard Jimenez Deleón
#Carnet: 7590-25-10502
#Sección: B
#Actualizacion: 05/09/2025

# Gestor de Notas Académicas

#Menu principal del gestor de notas y sus opciones
def mostrar_menu():
    print("="*80)
    print("GESTOR DE NOTAS ACADEMICAS")
    print("="*80)
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
    print("="*80)
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
            print("="*80)
            print("Saliendo del gestor de notas. ¡Hasta luego!")
            print("="*80)
            break
        else:
            print("="*80)
            print("Opción no válida. Por favor, seleccione una opción del 1 al 13.")
            print("="*80)

# Lista de cursos 
cursos = []
# Pila para historial de cambios
historial_cambios = []
# Cola para solicitudes de revisión (implementada con lista, no con deque)
cola_revisiones = []

# Esta funcion registra un nuevo curso y permite ingresar su nota
def registrar_curso():
    print("="*80)
    print("REGISTRAR NUEVO CURSO")
    print("="*80)

    codigo = input("Ingrese el código del curso (ej. 008): ")

    for curso in cursos:
        if curso['codigo'] == codigo:
            print(f"Ya existe un curso con el código {codigo}. No se puede registrar duplicados.")
            print("="*80)
            return

    nombre = input("Ingrese el nombre del curso: ")
    try:
        nota = int(input("Ingrese la nota del curso: "))
        if nota < 0 or nota > 100:
            print("Nota inválida. Debe estar entre 0 y 100.")
            print("="*80)
            return
    except ValueError:
        print("Entrada inválida. La nota debe ser un número.")
        print("="*80)
        return

    curso = {'codigo': codigo, 'nombre': nombre, 'nota': nota}
    cursos.append(curso)
    historial_cambios.append(f"Se registró el curso {codigo} '{nombre}' con nota {nota}.")
    print(f"Curso {codigo} '{nombre}' con nota {nota} registrado exitosamente.")
    print("="*80)

# Esta funcion permite mostrar los cursos y sus notas
def mostrar_cursos():
    print("="*80)
    print("MOSTRAR CURSOS Y NOTAS")
    print("="*80)
    if not cursos:
        print("No hay cursos registrados.")
    else:
        for curso in cursos:
            print(f"Código: {curso['codigo']}, Curso: {curso['nombre']}, Nota: {curso['nota']}")
    print("="*80)

# Esta funcion permite calcular el promedio general de las notas
def calcular_promedio():
    print("="*80)
    print("CALCULAR PROMEDIO GENERAL")
    print("="*80)
    if not cursos:
        print("No hay cursos registrados para calcular el promedio.")
    else:
        total_notas = sum(curso['nota'] for curso in cursos)
        promedio = total_notas / len(cursos)
        print(f"El promedio general de las notas es: {promedio:.2f}")
    print("="*80)

#Esta funcion permite contar los cursos que fueron aprobados/reprobados
def contar_aprobados_reprobados():
    print("="*80)
    print("CONTAR CURSOS APROBADOS Y REPROBADOS")
    print("="*80)
    if not cursos:
        print("No hay cursos registrados para contar aprobados y reprobados.")
    else:
        aprobados = sum(1 for curso in cursos if curso['nota'] >= 60)
        reprobados = len(cursos) - aprobados
        print(f"Cursos aprobados: {aprobados}, Cursos reprobados: {reprobados}")
    print("="*80)

# Esta funcion permite buscar un curso por su nombre usando búsqueda lineal
def buscar_curso_lineal():
    print("="*80)
    print("BUSCAR CURSO POR NOMBRE (LINEAL)")
    print("="*80)
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ")
    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscar.lower():
            print(f"Curso encontrado: {curso['codigo']} - {curso['nombre']}, Nota: {curso['nota']}")
            print("="*80)
            return
    print("Curso no encontrado.")
    print("="*80)

# Esta funcion permite actualizar la nota de un curso existente 
def actualizar_nota():
    print("="*80)
    print("ACTUALIZAR NOTA DE UN CURSO")
    print("="*80)
    codigo_actualizar = input("Ingrese el código del curso a actualizar: ")
    for curso in cursos:
        if curso['codigo'] == codigo_actualizar:
            try:
                nueva_nota = int(input(f"Ingrese la nueva nota para '{curso['nombre']}': "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("Nota inválida. Debe estar entre 0 y 100.")
                    print("="*80)
                    return
                anterior = curso['nota']
                curso['nota'] = nueva_nota
                historial_cambios.append(
                    f"Se actualizó {curso['codigo']} '{curso['nombre']}' de nota {anterior} a {nueva_nota}."
                )
                print(f"Nota del curso {curso['codigo']} '{curso['nombre']}' actualizada a {nueva_nota}.")
                print("="*80)
                return
            except ValueError:
                print("Entrada inválida. La nota debe ser un número.")
                print("="*80)
                return
    print("Curso no encontrado.")
    print("="*80)

# Esta funcion permite eliminar un curso por su código
def eliminar_curso():
    print("="*80)
    print("ELIMINAR CURSO")
    print("="*80)
    codigo_eliminar = input("Ingrese el código del curso a eliminar: ")
    for i, curso in enumerate(cursos):
        if curso['codigo'] == codigo_eliminar:
            eliminado = cursos.pop(i)
            historial_cambios.append(
                f"Se eliminó el curso {eliminado['codigo']} '{eliminado['nombre']}' con nota {eliminado['nota']}."
            )
            print(f"Curso {codigo_eliminar} eliminado exitosamente.")
            print("="*80)
            return
    print("Curso no encontrado.")
    print("="*80)

# Ordena cursos por nota usando burbuja 
def ordenar_por_nota():
    print("="*80)
    print("ORDENAR CURSOS POR NOTA (BURBUJA)")
    print("="*80)
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
    print("="*80)

# Ordena cursos por nombre usando inserción
def ordenar_por_nombre():   
    print("="*80)
    print("ORDENAR CURSOS POR NOMBRE (INSERCIÓN)")
    print("="*80)
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
    print("="*80)

# Búsqueda binaria por código
def buscar_curso_binaria():
    print("="*80)
    print("BUSCAR CURSO POR CODIGO (BINARIA)")
    print("="*80)
    if not cursos:
        print("No hay cursos registrados para buscar.")
        print("="*80)
        return

    cursos.sort(key=lambda x: x['codigo'])  
    codigo_buscar = input("Ingrese el código del curso a buscar (ej. 008): ")
    izquierda, derecha = 0, len(cursos) - 1             
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if cursos[medio]['codigo'] == codigo_buscar:
            print(f"Curso encontrado: {cursos[medio]['codigo']} - {cursos[medio]['nombre']}, Nota: {cursos[medio]['nota']}")
            print("="*80)
            return
        elif cursos[medio]['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Curso no encontrado.")   
    print("="*80)

# Simula cola de revisiones (FIFO)
def simular_cola_revisiones():
    print("="*80)
    print("SIMULACION DE COLA DE REVISIONES")
    print("="*80)
    while True:
        print("\n1. Agregar solicitud")
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
                procesado = cola_revisiones.pop(0)
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
            print("="*80)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.") 
    print("="*80)

# Historial de cambios (PILA)
def mostrar_historial_cambios():
    print("="*80)
    print("HISTORIAL DE CAMBIOS")
    print("="*80)
    if not historial_cambios:
        print("No hay cambios en el historial.")
    else:
        for cambio in reversed(historial_cambios):
            print(f"- {cambio}")
    print("="*80)

if __name__ == "__main__":
    main()
