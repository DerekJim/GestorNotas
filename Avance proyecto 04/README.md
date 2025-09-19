# EXPLICACIÓN DE CODIGO 

La función eliminar_curso() tiene como tarea principal gestionar la eliminación de cursos activos los cuales fueron ingresados anteriormente por el usuario, Ademas todos los cambios realizado quedaran registrados en un historial lo cual permite mantener un mejor control en las modificaciones del sistema.

* Busca el curso en la lista de cursos.
* Elimina el curso si es encontrado usando pop().
* La eliminacion se registra en el historial de cambios (historial_cambios).
* Se muestra un mensaje indicando que la eliminación fue realizada exitosamente o si el curso no fue encontrado.

### Función eliminar_curso() 


<span style="color: #27AE60">def eliminar_curso():</span>
    
##### 1. El programa pide al usuario ingresar el código del curso que desea eliminar.
    print("---------------------------------------------")
    codigo_eliminar = input("Ingrese el código del curso a eliminar: ")



##### 2. Se recorre la lista cursos. Por medio del bucle for (i) recorre la lista de cursos en cada iteración.
    for i, curso in enumerate(cursos):
        if curso['codigo'] == codigo_eliminar:

##### 2.1 La condición (if) verifica si el codigo del curso actu coincide con el código que el usuario quier eliminar
    for i, curso in enumerate(cursos):
        if curso['codigo'] == codigo_eliminar:



##### 3 Se elimina el curso usando pop(i), que además devuelve el curso eliminado para poder registrarlo en el historial.
            eliminado = cursos.pop(i)


##### 4 Se guarda un mensaje en la lista historial_cambios con detalles del curso eliminado: código, nombre y nota          
            historial_cambios.append(
                "Se eliminó el curso {eliminado['codigo']} '{eliminado['nombre']}' con nota {eliminado['nota']}."
            )


##### 5 Se muestra un mensaje al usuario que se elimino el curso exitosamente
            print("Curso {codigo_eliminar} eliminado exitosamente.")
            print("---------------------------------------------")
            return

##### 6 Se muestra al usuario un mensaje que el curso no fue encontrado       
    print("Curso no encontrado.")
    print("---------------------------------------------")