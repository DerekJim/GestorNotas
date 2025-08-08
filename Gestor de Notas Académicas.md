# Gestor de Notas Académicas

## Redacción del problema

El Gestor de Notas Académicas es un sistema diseñado para ayudar a estudiantes universitarios a organizar y analizar su rendimiento académico. El sistema permite registrar, consultar, modificar y analizar las calificaciones obtenidas en los diferentes cursos matriculados durante un semestre.

El objetivo principal es proporcionar al estudiante una herramienta sencilla pero poderosa para llevar un control detallado de su progreso académico, incluyendo cálculo de promedios, conteo de cursos aprobados/reprobados, y funciones de búsqueda y ordenamiento para facilitar el análisis de su desempeño.

## Requisitos del sistema

### Funcionales:
1. Registrar un nuevo curso y nota (validando que la nota esté entre 0-100)
2. Mostrar todos los cursos registrados con sus respectivas notas
3. Calcular y mostrar el promedio general de todas las notas
4. Contar y mostrar la cantidad de cursos aprobados (nota ≥ 60) y reprobados

### No funcionales:
- El sistema se ejecutará en consola utilizando Python 3.x
- No se utilizarán librerías externas, solo funcionalidades básicas del lenguaje
- Se implementará usando estructuras de control (bucles, condicionales), listas y funciones
- El menú principal funcionará en un bucle repetitivo hasta que el usuario elija salir