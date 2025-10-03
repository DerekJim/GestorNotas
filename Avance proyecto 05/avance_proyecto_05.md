# 📘 Avance de Proyecto 05 - Gestor de Notas Académicas

**Alumno:** Derek Stuard Jimenez Deleón  
**Carnet:** 7590-25-10502  
**Sección:** B  
**Fecha de actualización:** 05/09/2025  

Este proyecto implementa un **Gestor de Notas Académicas** en Python, aplicando estructuras de datos y algoritmos clásicos como: **pilas, colas, burbuja e inserción**.

---

## 🔄 Pilas (Historial de Cambios)

**Concepto:** Una pila es una estructura **LIFO** (*Last In, First Out*), donde el último elemento agregado es el primero en salir.  

**Implementación en el proyecto:**
- Variable: `historial_cambios = []`  
- Cada vez que se registra, actualiza o elimina un curso, se guarda el evento en la pila.  
- Función principal: `mostrar_historial_cambios()`.

**Ejemplo de uso:**
1. Registrar curso.
2. Actualizar nota.
3. Eliminar curso.  
##### Al mostrar el historial, se visualizan los cambios más recientes primero.

```python
def mostrar_historial_cambios():
    if not historial_cambios:
        print("No hay cambios en el historial.")
    else:
        for cambio in reversed(historial_cambios):
            print(f"- {cambio}")
```

---

## 📥 Colas (Solicitudes de Revisión)

 **Concepto:** Una cola es una estructura **FIFO** (*First In, First Out*), donde el primer elemento agregado es el primero en procesarse.  

 **Implementación en el proyecto:**
- Variable: `cola_revisiones = []`  
- Función `simular_cola_revisiones()` permite:
  1. Agregar solicitudes con `append()`.
  2. Procesar solicitudes con `pop(0)`.
  3. Mostrar el estado actual de la cola.

 **Ejemplo de uso:**
- Se agregan varias solicitudes de revisión.  
- Se procesan en orden de llegada.  
- Se muestran las pendientes.

```python
def simular_cola_revisiones():
    cola_revisiones.append("Curso 001")  # Agregar
    procesado = cola_revisiones.pop(0)   # Procesar
```

---

## 📊 Ordenamientos

### 🔹 3.1 Burbuja (Bubble Sort)

**Uso:** Ordenar cursos por **nota** de menor a mayor.  
**Funcionamiento:** Compara elementos adyacentes e intercambia posiciones si están en orden incorrecto, repitiendo el proceso hasta ordenar la lista.  
**Implementación:** opción 8 del menú → `ordenar_por_nota()`.

```python
def ordenar_por_nota():
    n = len(cursos)
    for i in range(n):
        for j in range(0, n-i-1):
            if cursos[j]['nota'] > cursos[j+1]['nota']:
                cursos[j], cursos[j+1] = cursos[j+1], cursos[j]
```

---

### 🔹 3.2 Inserción (Insertion Sort)

 **Uso:** Ordenar cursos por **nombre alfabéticamente**.  
 **Funcionamiento:** Inserta cada elemento en la posición correcta dentro de la parte ya ordenada de la lista.  
 **Implementación:** opción 9 del menú → `ordenar_por_nombre()`.

```python
def ordenar_por_nombre():
    for i in range(1, len(cursos)):
        key = cursos[i]
        j = i-1
        while j >= 0 and key['nombre'].lower() < cursos[j]['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
```

---

## ✅ Conclusión

Este proyecto demuestra el uso práctico de estructuras de datos y algoritmos básicos:

- **Pilas** → para el historial de cambios.
- **Colas** → para gestionar solicitudes de revisión.
- **Ordenamientos (burbuja e inserción)** → para organizar cursos y notas.

 Gracias a estas implementaciones, el sistema es capaz de gestionar información de manera organizada, eficiente y clara.

