# Proyecto Urban Grocers - API Test Automation Suite


## 1. Descripción
Este proyecto contiene una suite de pruebas automatizadas desarrolladas en Python para validar el comportamiento de la API de **Urban Grocers**, específicamente enfocado en el endpoint de creación de kits (`/api/v1/kits`). 

El objetivo principal es verificar de forma automatizada las reglas del campo `name` (nombre del kit), asegurando que el sistema acepte los valores válidos (como límites de caracteres, números y caracteres especiales) y rechace correctamente las solicitudes inválidas (como campos vacíos, tipos de datos incorrectos o parámetros faltantes) mediante códigos de respuesta HTTP como `201 Created` y `400 Bad Request`.

---

## 2. Fuente de Documentación Utilizada
Para el diseño de los casos de prueba y la comprensión de la estructura de las solicitudes/respuestas de la API, se utilizó la documentación oficial de la plataforma generada a través de **apiDoc**. 

A partir de esta documentación técnica se extrajeron:
* Las rutas y métodos HTTP requeridos (ej. `POST /api/v1/kits`).
* Los encabezados obligatorios de autenticación (`"Authorization": "Bearer {authToken}"`).
* Los body requeridos en JSON (`{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"}`).

---

## 3. Descripción de las Tecnologías y Técnicas Utilizadas

### Tecnologías:
* **Python 3.x:** Lenguaje de programación principal debido a su legibilidad y robustez para scripts de automatización.
* **Pytest:** Framework de pruebas de software utilizado para estructurar las funciones de prueba, gestionar la ejecución y generar los reportes de resultados.
* **Requests:** Librería HTTP para Python empleada para interactuar directamente con la API mediante el envío de solicitudes y la captura de respuestas JSON.

### Técnicas de Prueba Aplicadas:
* **Análisis de Valores Límite (Boundary Value Analysis):** Técnica utilizada para definir los casos de prueba en los extremos exactos permitidos por la documentación (ej. nombres de 1, 511 y 512 caracteres) para detectar fallos en las fronteras del sistema.
* **Partición de Clases de Equivalencia (Equivalence Partitioning):** Aplicada para agrupar entradas válidas e inválidas en clases (strings normales, caracteres especiales, campos vacíos, tipos de datos numéricos enteros) y evaluar el comportamiento del sistema con representantes de cada clase.
* **Pruebas Positivas y Negativas:** Diseño de escenarios para comprobar que el sistema hace lo que se supone que debe hacer (201 Created) y reacciona de manera controlada ante lo que no debe permitir (400 Bad Request).

---

## 4. Dependencias Necesarias
Para la correcta ejecución del proyecto, se necesitan las siguientes librerías de Python:
* **pytest** (Gestión de pruebas)
* **requests** (Solicitudes HTTP)

---

## 5. ¿Cómo instalar las dependencias?
Abre la terminal en la carpeta raíz de este proyecto y ejecuta el siguiente comando:

```bash
pip install requests pytest
````

---

## 6. ¿Cómo ejecutar el proyecto?
Para correr todas las pruebas automatizadas y verificar los resultados en la consola, ejecuta el siguiente comando en la terminal:

```bash
pytest -v create_kit_name_kit_test.py
````