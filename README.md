# Finance.py
Calculadora de Gastos
Una aplicación en Python para rastrear ingresos y gastos personales, con funcionalidades para categorizar gastos, mostrar resúmenes financieros y generar gráficos de gastos por categoría.
Descripción
La Calculadora de Gastos es una herramienta de línea de comandos que permite a los usuarios:

Registrar ingresos y gastos.
Organizar gastos por categorías (Comida, Transporte, Entretenimiento, Servicios, Otros).
Ver un resumen financiero con ingresos, gastos totales y saldo.
Generar un gráfico circular que muestra la distribución de gastos por categoría.
Guardar los datos en un archivo JSON para persistencia.

El proyecto utiliza bibliotecas como matplotlib para visualización, colorama para salida en colores, y json para almacenamiento de datos.
Requisitos

Python 3.6 o superior
Bibliotecas de Python:
matplotlib
colorama



Instalación

Clona el repositorio:
git clone https://github.com/jokerjaas2002/Calculadora-de-gastos.git
cd Calculadora-de-gastos


Crea un entorno virtual (opcional, pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


Instala las dependencias:
pip install matplotlib colorama



Uso

Ejecuta el programa:
python expense_tracker.py


Selecciona una opción del menú:

1. Agregar Ingreso: Ingresa un monto para añadir a tus ingresos.
2. Agregar Gasto: Ingresa el monto, categoría y una descripción opcional para un gasto.
3. Mostrar Resumen: Muestra un resumen de ingresos, gastos totales, saldo y gastos por categoría.
4. Graficar Gastos: Genera un gráfico circular de gastos por categoría y lo guarda como expenses_pie_chart.png.
5. Salir: Cierra la aplicación.



Ejemplo de Interacción
=== Personal Expense Tracker ===
1. Add Income
2. Add Expense
3. Show Summary
4. Plot Expenses
5. Exit
Select an option: 1
Enter income amount: 1000
Added $1000.00 to income. New balance: $1000.00

Estructura del Proyecto

expense_tracker.py: Código principal de la aplicación.
expenses.json: Archivo generado automáticamente para almacenar los datos de ingresos y gastos.
expenses_pie_chart.png: Gráfico generado al usar la opción "Graficar Gastos".

Características

Persistencia de Datos: Los datos se guardan en expenses.json para mantener el historial entre sesiones.
Validación de Entradas: Verifica que los montos sean válidos y las categorías sean correctas.
Interfaz Colorida: Usa colorama para una salida visualmente atractiva en la consola.
Visualización de Datos: Genera gráficos circulares con matplotlib para analizar gastos.

Contribuir

Haz un fork del repositorio.
Crea una rama para tu característica (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -m "Añadir nueva característica").
Empuja tus cambios (git push origin feature/nueva-caracteristica).
Abre un Pull Request en GitHub.

Licencia
Este proyecto está bajo la Licencia MIT.
Contacto
Si tienes preguntas o sugerencias, contáctame en jokerjaas2002@example.com o abre un issue en el repositorio.
