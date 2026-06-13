# 🚀 MODELO DE CLAVES BOOLEANAS — RECUPERACIÓN DE INFORMACIÓN



## 🏛️ Instituto Tecnológico Beltrán (ISFT Nº 197)

### 📘 Cátedra: Técnicas de Procesamiento del Habla



---

## 👥 Datos Académicos

* 👩‍💻 **Alumna:** Silvana Alejandra Gerez  
* 👩‍🏫 **Profesora:** Yanina Escudero  
* 🎓 **Carrera:** Técnico Superior en Ciencia de Datos e Inteligencia Artificial  
* 📅 **Año Académico:** 2026 — 2.º Año  

---



## 🧠 1. ¿De qué se trata este proyecto? (El valor de construir desde cero)

El objetivo de este proyecto es entender y programar el corazón de un Sistema de Búsqueda Exacta utilizando el **Modelo de Claves Booleanas**. Este paradigma matemático se basa en el **Álgebra de Boole** y la **Teoría de Conjuntos** para definir si un documento es relevante (1) o se descarta (0) frente a lo que busca el usuario, combinando palabras clave con los conectores lógicos **AND**, **OR** y **NOT**.

⚠️ **El gran valor técnico de esta entrega:** Hoy en día existen herramientas industriales avanzadas como **Elasticsearch** que resuelven esto de forma automatizada. Sin embargo, en este proyecto **no usamos soluciones empaquetadas**. Decidimos apoyarnos en la librería fundacional **NLTK (Natural Language Toolkit)** para sus tareas esenciales de texto y construir toda la lógica del motor a mano. 

Esto nos obligó a diseñar artesanalmente cada etapa del procesamiento y la estructura de almacenamiento. Además, demuestra una propiedad clave en la Ciencia de Datos: la **independencia del dominio**. El mismo motor lógico abstracto procesa y resuelve búsquedas con idéntica velocidad sobre un corpus de Inteligencia Artificial que sobre textos de Civilizaciones Antiguas.



---

## 🛠️ 2. ¿Cómo el Código Procesa el Texto Paso a Paso?

Al trabajar a bajo nivel con **NLTK**, el texto en bruto pasa por una serie de filtros y ordenamientos lógicos controlados por nuestro código:



### 🔀 Paso A: Tokenización y Normalización (Separar y Unificar)

Utilizando la función `word_tokenize` de **NLTK**, el programa toma las oraciones largas y las corta en palabras individuales llamadas **tokens**. En ese mismo proceso, convertimos todo a minúsculas (`.lower()`).

* *¿Por qué importa?* Porque unifica el vocabulario. Así, no importa si el usuario escribe "Egipcios", "egipcios" o "EGIPCIOS"; para el motor siempre será el mismo término y la búsqueda nunca fallará por problemas de tipeo.



### 🚫 Paso B: Filtrado Estructural y Remoción de Ruido (*Stop Words*)

Los textos están llenos de palabras que sirven para conectar ideas pero que no tienen peso temático. Nuestro código hace una limpieza profunda:

1. **Filtro Alfanumérico (`word.isalnum()`):** Elimina puntos, comas y signos que romperían la coincidencia exacta de los términos.

2. **Remoción de Palabras Vacías:** Usamos de forma directa el diccionario de *stopwords* en español de **NLTK** para identificar y descartar artículos, preposiciones y conectores (como "el", "la", "un", "y"). Al limpiar este ruido, el sistema se queda únicamente con las palabras valiosas que definen el significado del texto.



### 🗂️ Paso C: Construcción del Índice Invertido (La Base del Buscador)

Buscar una palabra leyendo todos los documentos uno por uno cada vez que el usuario pregunta sería lento e ineficiente. Para resolver esto, implementamos la estructura estrella de la recuperación de información: el **Índice Invertido**, guardado en memoria mediante un diccionario de Python.

* *¿Cómo funciona?* Es exactamente igual al índice analítico que encontrás al final de un libro de estudio. El programa registra cada palabra única del vocabulario purificado y le asocia un conjunto dinámico (`set`) con los números de documentos donde aparece. Así, la localización es instantánea.



### 📐 Paso D: Consulta Operacional (Álgebra de Conjuntos)

Cuando se ingresa una consulta en la terminal, el motor de búsqueda evalúa los términos de izquierda a derecha. Al detectar los operadores en mayúsculas (`AND`, `OR`, `NOT`), realiza operaciones lógicas directamente sobre los conjuntos del índice invertido:

* **AND (Intersección `&=`):** Devuelve solo los documentos donde coexisten todas las palabras buscadas al mismo tiempo.

* **OR (Unión `|=`):** Suma los resultados para mostrar todo lo que coincida con cualquiera de los términos.

* **NOT (Diferencia `-=`):** Resta y excluye de forma tajante cualquier documento que contenga la palabra prohibida.



---

## 📁 3. Estructura del Repositorio

* 📄 **`Claves Booleanas Consigna 1.py`**
* 📄 **`Claves Booleanas Consigna 2.py`**

---

## 🚀 4. Requisitos

* 🐍 **Python 3.x**
* 🛠️ **Visual Studio Code**
* 📦 **Librería NLTK**



---

## 💻 5. Guía de Uso Rápido

Al ejecutar los scripts en la terminal de Visual Studio Code, el sistema se quedará esperando tu consulta. Recordá escribir los operadores lógicos en mayúsculas.

