# 1.	Introducción 

ANALISIS, DISEÑO, DESARROLLO E IMPLEMENTACION DE UNA APLICACION WEB EN LA FARMACIA (Famisalud La 91) PARA LA ORGANIZACION Y VENTA VIRTUAL DE UNA FARMACIA.

## 1.1	Propósito

El propocito de esté, es describir lo acordado con el cliente y crear paso a paso el sofware que servira para llevar a cabo el inventario y la venta de los productos que la farmacia ofrece, al sistematizar  estos procesos tendremos un mejor redimiento en el area inventario y venta.

## 1.2	alcance:

Realizaremos una tienda virtual con inventario, que permitira llevar el control sobre la entrada y salida de los productos que se registran en la farmacia (famisalud la 91), se llevara a cabo la venta de estos mismos todo esto con el fin de poder mejorar las ventas y la organizacion, en este proyecto no realizaremos la instalacion ni haremos el mantenimiento del software.  

## 1.3	definir, acrónimo y abreviatura

SENA: Servicio Nacional de Aprendizaje.

Sofia: Sistema Optimizado para la formación Integral del Aprendizaje Activo.

Base de datos: una base de datos se encarga no solo de almacenar datos, sino tambien de conectarlos entre si en una unidad logica.

Software: Estos son los programas informáticos que hacen posible la ejecución de tareas específicas dentro de un computador. Por ejemplo, los sistemas operativos, aplicaciones, navegadores web, juegos o programas.

inventario: El inventario es la comprobación manual de que las cantidades físicas y reales en stock de cada producto de nuestra farmacia coinciden con las cantidades de cada producto registradas en el programa informático de gestión.

Firewall: es un sistema de seguridad de red de las computadoras que restringe el tráfico de Internet entrante, saliente o dentro de una red privada.

Requerimientos funcionales: describen las capacidades o funciones que el sistema será capaz de realizar.

Requerimientos no funcionales: restricciones o características que de delimitan el sistema, como por ejemplo, rendimiento, interfaces de usuario, fiabilidad, seguridad, portabilidad, normas, entre otros.

## 1.4	referencia

https://edu.gcfglobal.org/es/informatica-basica/que-es-hardware-y-software/1/

https://www.arimetrics.com/glosario-digital/base-de-datos

https://www.mcafee.com/es-co/antivirus/firewall.html

http://www.pmoinformatica.com/2018/05/que-es-requerimiento-funcional.html

https://visuresolutions.com/es/blog/non-functional-requirements/

## 1.5	Apreciación global

En este documento se presenta una introducción corta .
Dónde en la siguiente parte se puede ver la perspectiva del proyecto, con sus funciones, especificaciones y características del proyecto mismo y de sus futuros usuarios. 
En el punto 3 se presenta una especificación detallada de requerimientos que son necesarios para el análisis, diseño, desarrollo e implementación del sistema.


# 2.	Descripción General

## 2.1	Perspectivas del Producto

-  Con este software se espera una mejora en la forma de cómo se maneja parte de la venta y parte del inventario en la farmacia famisalud la 91.
- Dicho inventario será la mejor manera de llevar la informacion de las ventas y el registro de los productos 
## 2.2	Funciones del Producto
- Registrar cliente.
- Registrar producto.
- Registrar detalles de compra.
- Registrar productos de ingreso.
- Registrar productos de salida.
- Registrar detalle de pedido.
- Visualizacion de productos disponibles.
- Generar reporte de productos escasos.

## 2.3	Características de Usuario

- Los usuarios seran los clientes, los empleados y los administradores.

- Los clientes trendan acceso a la visualizacion y compra de los productos que se encuentren disponibles.
- Los empleados tendra a acceso al registro de los productos que ingresan y salen de la farmacia y al apartado de los pedidos y las ventas realizadas en fisico.
- El administrador tendra acceso a las ventas y al registro de los productos.

## 2.4	Restricciones

- Para este sistema las posibles restricciones son el tiempo que tomará el desarrollo de este, recursos donde se implantara el sistema, el nivel del lenguaje programación para los desarrolladores

## 2.5	Atención y Dependencias

- El sistema llevara el registro de las ventas, el inventario, el registro de los pedidos y el registro de los clientes. 
	
# 3.	Requerimientos Específicos 

## 3.1	Requerimientos Funcionales

|Codigo                  | PF001                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Registro de Inventario                  |
| Fecha                  | 04/ 27 / 2023                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | Debe permitir al administrador mostrar los productos y la cantidad con la que dispone de cada uno de estos |
| Entrada                | Gmail, Contraseña                       |
| Fuente                 | Administrador                           |
| Salida                 |  emcabezado de inventario             |
| Destino                | Regitro con la cantidad disponible de cada producto   |
| Restriccion          | Solo el personal administrativo que cuente con ususario valido puede ingresar y visualizar dicha informacion | 
| Efecto colateral       | Esto le brinda al administrador un mejor manejo de todos sus productos dándole mayor eficiencia a la hora de llevar un conteo de todo los productos que entran y salen de la empresa y las ganancias que estos dejan | 

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- ingresa usuario                                                                           |
|- verifica que el ususario sea correcto                                                     |
|- si el ususario es incorrecto vuelve a pedirlo                                             |
|- si es usuario es correcto ingresa                                                         |
|- muestra un regitro de todos los productos con la cantidad disponible de cada uno de estos |

|Codigo                  | PF002                                   |
|------------------------|-----------------------------------------|
| Nombre                 | inicio de sesion                        |
| Fecha                  |  04 / 07 / 2023                         |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | Debe permitir al usuario iniciar sesion con un tipo de usuario ya sea (Administrador, empleado o cliente) |
| Entrada                | tipo de ususario, identificacion y contraseña                        |
| Fuente                 | Usuario                                 |
| Salida                 | Mensaje al correo validando que se inicio sesion correctamente |
| Destino                | pagina principal                        |
| Restriccion          | dos o mas usuarios no pueden utilizar la misma identificacion | 
| Efecto colateral       | no se desplegaria pagina principal                             | 

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Registrarse en el sistema                                                                 |
|- Omitir el regitro si ya se encuentra en el sistema                                        |
|- Inicia seccion                                                                            |
|- Verificar que se inicie seccion correctamente                                             |
|- Visualiza la pagina principal                                                             |

|Codigo                  | PF003                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Modulo de carrito                       |
| Fecha                  |  04 / 07 / 2023                              |
| Grado de nesecidad     | media                                   |
| Descripcion            |permite al usuario agregar productos al carrito y apartar un producto sin la nesecidad de llevarselo enseguida |
| Entrada                | boton (agregar al carrito)                     |
| Fuente                 | base de datos                           |
| Salida                 | Mansaje de producto agregado al carrito |
| Destino                | carrito con la informacion de los productos agregados (nombre del Producto, descripcion, foto, cantidad, precio, codigo deproducto, fecha)       |
| Restriccion            | debe de estar registrado para poder agregar productos al carrito | 
| Efecto colateral       | sin productos en el carrito no habra compra |

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Inica seccion                                                                             |
|- se verifica que el inicio de seccion este correcto                                        |
|- escoge el producto a comprar                                                              |
|- Ingresa producto al carrito                                                               |       
|- hace un apartado del producto a comprar determinando la fecha que vendra por este. (Opcional )   |


|Codigo                  | PF004                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Registro de usuario                     |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            |permite al usuario registrase en el sistema, como cuenta tipo (usuario) |
| Entrada                | nombre, apellidos,  identificacion, direccion, correo, contraseña                     |
| Fuente                 | usuario                                |
| Salida                 | mensaje de registro exitoso            |
| Destino                | modulo metodo de pago                   |
| Restriccion            | no debe haber dos cuentas con el mismo correo | 
| Efecto colateral       | no se podria llevar a cabo ningun tipo de compra |


|Codigo                  | PF005                                   |
|------------------------|-----------------------------------------|
| Nombre                 | modulo metodo de pago                          |
| Fecha                  |  04 / 07 / 2023                              |
| Grado de nesecidad     | Alto                                    |
| Descripcion            |permite al usuario seleccionar la forma de pago del producto|
| Entrada                | efectivo y tarjeta |
| Fuente                 | usuario                                |
| Salida                 | mensaje via gmail                      |
| Destino                | modulo de factura                   |
| Restriccion          | es obligario seleccionar un metodo de pago | 
| Efecto colateral       | no seria posible escoger la forma de pago del producto |


|Codigo                  | PF006                                   |
|------------------------|-----------------------------------------|
| Nombre                 |  modulo de Productos                               |
| Fecha                  |  04 / 07 / 2023                              |
| Grado de nesecidad     | Alto                                    |
| Descripcion            |detalles de cada producto para su organizacion |
| Entrada                | nombre, Codigo, Cantidad                       |
| Fuente                 | Empleado                                |
| Salida                 | Producto añadido                        |
| Destino                | Inventario (nombre, Codigo, Cantidad)   |
| Restriccion          | Solo los empleados/administrador Pueden Ingresar a este requerimiento |
| Efecto colateral       | NO Ingresar Los datos de producto al inventario y Solicitar los datos nuevamente |


|Codigo                  | PF007                                   |
|------------------------|-----------------------------------------|
| Nombre                 | main                                    |
| Fecha                  |  04 / 07 / 2023                         |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | en este requerimiento se va a organizar la pagina principal a la cual se van a acceder los usuarios despues de iniciar sesion |
| Entrada                | inicio de sesion                        |
| Fuente                 | base de datos                                 |
| Salida                 |    |
| Destino                | main                                    |
| Restriccion          | tiene que estar logueado para poder acceder a este apartado | 
| Efecto colateral       | manda al cliente a iniciar sesion en su cuenta o a que se registre                            | 




## 3.2 resquerimirntos no funcionales 
| codigo     | nombre                    | fecha       | grado necesida |
|------------|---------------------------|-------------|----------------|
| PF004      | Rendimiento del programa  | No registra | Alto           |
|descripcion | El programa debe tener el mejor rendimiento, la mejor velocidad de carga y el mejor desenpeño posible para dar una buena satisfaccion a cada uno de los usuarios |


| codigo     | nombre                    | fecha       | grado necesida |
|------------|---------------------------|-------------|----------------|
| PF005      | proteccion de informcion  | No registra | Alto           |
|descripcion | El programa de garantizar la seguridad de la informcion que los usuarios ingresan |


| codigo     | nombre                      | fecha       | grado necesida |
|------------|-----------------------------|-------------|----------------|
| PF005      | sostenibilidad del programa | No registra | Alto           |
|descripcion | El programa debe tener la capacidad de mantenerse activo y funcionando a su 100%, si llega a presentar algun fallo debe ser capaz de recuperarse en el menor tiempo posible sin afectar de ninguna forma al usuario |


## 3.3 requerimientos de interfaz de usuario 
| codigo      | nombre              | fecha       | grado necesida |
|-------------|---------------------|-------------|----------------|
| PF006       | Almacen de registro | No registra | Alto           |
| descripcion | permitira guardar la informcaion del ususario al regitrarse en el sistema |


| codigo      | nombre         | fecha       | grado necesida |
|-------------|----------------|-------------|----------------|
| PF007       | ingreso y uso  | No registra | Alto           |
| descripcion | el programa debe terner un acceso y un uso facil para los usuarios |


| codigo      | nombre             | fecha       | grado necesida |
|-------------|--------------------|-------------|----------------|
| PF008       | registro de pedido | No registra | Alto           |
| descripcion | Se guardara un registro de cada uno de los pedidos que se hagan |

# 4. Determinacion de las tecnologias de Hardware,Software y servicios requerido

## 4.1 Software

El software se creara utilizando el lenguaje de programacion (Python), para este trabajo utilizaremos la base de datos SQLite debido a su sencillez, eficacia asi como su rapides y usaremos a visual studio code como herramienta principal de desarrollo.

## 4.2 Hosting

el Hosting que utilizaremos en este trabajo no esta definido pero cabe resaltar que el servicio de hosting que se contrate debe tener la suficiente capacidad de almacenamiento para nuestro programa.

## 4.3 Computador

para desarrollar el software se debe contar con un computador sin importar el modelo de al menos un prosesador de 2.5 GHz y 6 nucleos, una Ran de 8 GB y un disco solido de 300 GB

## 4.4 Escaner Lector Codigo de Barras Automático Soporte USB Base
se requiere utilizar un escaner lector de barras, este debe tenre una buena calidad y tiene que ser de soporte USB

## 4.5 Router (Router Inalámbrico/Repetidor WiFi N300Mbps, Tp-Link TL-WR840N)

## 4.6 Presupuesto

No definido
