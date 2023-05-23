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


## Actividad 01: [Transportistas](/bases-de-datos/actividad-01/transportistas.sql)

De acuerdo al siguiente DER (Diagrama Entidad-Relación)

![](/docs/images/diagrama-entidad-relacion-transportistas.jpg?raw=true)

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


## Actividad 02: [Spotify](/bases-de-datos/actividad-02/spotify.sql)

⚠️ Para esta actividad se debe importar el siguiente recurso que se menciona a continuación, a partir de estos [pasos](#-pasos-para-importar-tablas-desde-archivos-csv-o-json).

En la carpeta de recursos se encuentra un archivo llamado Top_Spotify.csv. Se debe importar ese archivo a una base de datos creada con el nombre de PLAYLIST.

Tener a consideración las siguientes indicaciones:
* No cambiar el nombre de la tabla.
* Eliminar la tabla en el caso de que ya exista dentro de la base de datos.
* Mantener los tipos de datos asignados al momento de la importación.

Se deben resolver los siguientes ítems:
1. Mostrar todo el contenido de la tabla TOP_SPOTIFY importada en el paso anterior.
2. Ahora, en el resultado de la consulta, sólo se deben observar las columnas ARTISTA, TÍTULO y GÉNERO.
3. Ordenar alfabéticamente el resultado de la consulta según los géneros musicales.
4. En el caso de aquellos géneros que se repiten, ordenar alfabéticamente los nombres de los artistas.
5. En base al ejercicio anterior, mostrar todos los registros de la tabla TOP_SPOTIFY. En el resultado, sólo se deben observar las columnas ARTISTA, TÍTULO y GÉNERO. Ordenar el resultado alfabéticamente según los nombres de los artistas y el nombre de las canciones. Mostrar únicamente las 10 primeras canciones.
6. Modificar la consulta anterior para mostrar únicamente las canciones ubicadas desde la posición 11 hasta la 15 inclusive.
7. Dada la tabla TOP_SPOTIFY, obtener una lista de todas aquellas canciones pertenecientes a la cantante Lady Gaga. Debes mostrar todos los campos de la tabla en el resultado de la consulta.
8. A partir de la tabla TOP_SPOTIFY, obtener una lista de todas aquellas canciones pertenecientes al género Pop. Mostrar todos los campos de la tabla en el resultado de la consulta y ordenar alfabéticamente el resultado según el nombre de las canciones.
9. De la tabla TOP_SPOTIFY, obtener una lista de todas las canciones pertenecientes al género Pop lanzadas durante el año 2015. Mostrar todos los campos de la tabla en el resultado de la consulta y ordenar dicho resultado alfabéticamente según los nombres de los artistas y los nombres de las canciones.
10. A partir de la tabla TOP_SPOTIFY, obtener una lista de todas aquellas canciones lanzadas antes del año 2011 y que pertenezcan al género Dance Pop. Mostrar todos los campos de la tabla en el resultado de la consulta y ordenar dicho resultado alfabéticamente según los nombres de las canciones.


## Actividad 03: [Proveedores](/bases-de-datos/actividad-03/proveedores.sql)

Se debe corregir la consulta SQL para que retorne el número total de cada artículo enviado por cada proveedor junto con el nombre del proveedor y el id del artículo.

![](/docs/images/diagrama-entidad-relacion-proveedores.jpg?raw=true)

```bash
SELECT SUM(e.cantidad), p.nombre, e.id_articulo
FROM Proveedor p JOIN Envio e ON p.id_proveedor = e.id_proveedor
AND e.id_articulo IN (SELECT a.decripcion FROM Articulo a);
```