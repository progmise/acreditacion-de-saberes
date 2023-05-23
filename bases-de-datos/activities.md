# Bases de datos


## 📋 Pre-requisitos 

_XAMPP/WAMP y MySQL Workbench_


## 🔧 Pasos para importar tablas desde archivos CSV o JSON

**1. Pulsa el clic derecho del mouse sobre el nombre de la base de datos en uso**

**2. Seleccionar la opción "Table Data Import Wizard". Al seleccionar esta opción se mostrará la siguiente pantalla**

![](/docs/images/mysql-workbench-step-02.jpg?raw=true)

**3. Pulsar el botón "Browse"**

**4. Ubicar y abrir el archivo que contiene la tabla a importar**

**5. Pulsa el botón "Next"**

**6. Especificar si se quiere volcar los datos de la tabla importada en una tabla existente dentro de la base de datos, o seleccionar la opción "Create new table" para crear una nueva tabla dentro de la base de datos. Se puede cambiar el nombre de la tabla, o mantener el nombre por defecto (el nombre del archivo). Pulsar "Next"**

![](/docs/images/mysql-workbench-step-06.jpg?raw=true)

**7. En este paso, se puede especificar los tipos de dato para cada campo. Por defecto, MySQL Workbench asignará a cada campo (columna) un tipo de dato según los valores que encuentre en ellos**

**8. Una vez definidos los tipos de datos para cada campo, pulsar "Next"**

![](/docs/images/mysql-workbench-step-08.jpg?raw=true)

**9. En este paso, sólo se especifica que se llevará a cabo la importación de los datos desde el archivo de datos externo. Sólo bastará con pulsar "Next" para comenzar la importación**

![](/docs/images/mysql-workbench-step-09.jpg?raw=true)

**10. Finalizado el proceso de importación, pulsar el botón "Next" para poder observar la pantalla final. En esta vista se encontrará el tiempo que tardó la importación de los datos, la confirmación de que la tabla fue creada dentro de la base de datos y la cantidad de registros importados desde el origen externo**

**11. Pulsar "Finish" para concluir el asistente**

**12. Se deben actualizar los esquemas para observar la tabla dentro de la base**

![](/docs/images/mysql-workbench-step-12.jpg?raw=true)


## Actividad 01: [Transportistas](/bases-de-datos/actividad-01/empresa.py)

De acuerdo al siguiente DER (Diagrama Entidad-Relación)

![](/docs/images/diagrama-entidad-relacion.jpg?raw=true)

Se deben resolver los siguientes ítems:
1. Crear una base de datos llamada **"Transportista"**.
2. Crear las tablas y las relaciones que se muestran en la imagen.
3. Aplicar los tipos de datos como se detallan en la imagen.
d. Agregar:
    * 3 registros en la tabla **"Camiones"** (usar en Marca: SCANIA, FIAT, IVECO),
    * 3 registros en tabla **"Camioneros"** (DOMINGUEZ, MARTINEZ, ROBLEDO) y
    * 3 registros en la Tabla **"Ciudades"** (MENDOZA, MISIONES, SALTA).

En todos los casos, respetar los datos que se piden pues se utilizan en los puntos siguientes mientras que para el resto de datos puede ingresar cualquier otro.

4. Registrar el envío de 2 paquetes a la ciudad de MISIONES con el camión de Marca Fiat.
5. Registrar el envío de 2 paquetes a la ciudad de MENDOZA con el camión de Marca IVECO.
6. Modificar la Matrícula del camión SCANIA por 8795.
7. Calcular el monto de dinero que se paga en sueldos a todos los camioneros.
8. Listar por orden alfabético en forma ascendente, la cantidad de paquetes que transporta cada Camionero a la ciudad de SALTA.
9. Eliminar el registro del segundo paquete enviado a MENDOZA en el punto 6.

