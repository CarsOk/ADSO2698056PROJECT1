# 1.	Introducción 

## 1.1	Propósito

El objetivo de este proyecto es desarrollar de manera clara y precisa las funcionalidades que tendrá el sistema que se desea construir, y va dirigida al proyecto formativo y al empresario.

## 1.2	alcance:

 El sistema que se desea construir pretende mejorar la manera en que se opera el sistema actualmente y aumentar la cantidad de beneficios obtenidos con él.

Este sistema se encargará de facilitar las operaciones realizadas en la empresa (Famisalud la 91) de manera más fácil e eficiente, tales como las compras, ventas y el inventario.

## 1.3	definir, acrónimo y abreviatura

SENA: Servicio Nacional de Aprendizaje
Sofia: Sistema Optimizado para la formación Integral del Aprendizaje Activo

## 1.4	referencia

Para la realización de nuestro proyecto, solo hemos utilizado las especificaciones, e información facilitada por el empresario, y la información recolectada de los análisis planteados por nuestro equipo de trabajo.

## 1.5	Apreciación global

Este proyecto se hace con el fin de brindar la mayor satisfacción posible a la empresa, brindando el mejor rendimiento a los usuarios, así como optimizando las funciones del empresario.

# 2.	Descripción General

## 2.1	Perspectivas del Producto

-  La principal perspectiva de este proyecto es que ningún usuario tenga que tener amplio conocimiento para usar dicho software, además el software será diseñado para tener compatibilidad con cualquier dispositivo o pagina web, brindado un fácil uso a cualquiera de los usuarios beneficiarios de este proyecto.

## 2.2	Funciones del Producto

- El Sistema de Gestión del Almacén (SGA) es el software que automatizara los procesos y
permite integrar y administrar con eficacia todas las tareas operativas y logísticas de un
espacio de almacenaje, gestionando todos los movimientos, los materiales y la maquinaria
de trabajo de un almacén en cada una de las etapas logísticas llevadas a cabo, desde la
recepción de mercancías hasta el almacenamiento y la preparación de la empresa.

## 2.3	Características de Usuario

- ese software estará dirigido a la empresa(Famisalud la 91) y todos los usuarios, brindando la mayor accesibilidad a todas las personas que dispongan de dicho software.

## 2.4	Restricciones

- como minimo se debe hacer uso de los protocolos de intercambio de datos via internet.
respecto a la seguridad, se debe considerar el uso de sesiones para limitar el proceso a usuarios no autorizados.
el cliente no ha espesificado ningun otro limite, y algunas de las caracteristicas las dejo a los desarrolladores 

## 2.5	Atención y Dependencias

- este software tendrá una dependencia de acceso a internet para poder garantizar que este funcional, por otra parte se necesitara de un equipo para manejar el software.
	
# 3.	Requerimientos Específicos 

## 3.1	Requerimientos Funcionales

|Codigo                  | PF001                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Registro de Inventario                  |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | Debe permitir al adminidtrador mostrar los productos y la cantidad con la que dispone de cada uno de estos |
| Entrada                | Gmail, Contraseña                       |
| Fuente                 | Administrador                           |
| Salida                 |  emcabezado de la pagina                |
| Destino                | Regitro con la cantidad disponible de cada producto   |
| Restricciones          | Solo el personal administrativo que cuente con ususario valido puede ingresar y visualizar dicha informacion | 
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
| Nombre                 | Registro de usuarios                    |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | Debe permitir al usuario iniciar sesion con un tipo de usuario ya sea (Administrador, empleado o cliente) |
| Entrada                | Nombre, Apellidos, Telefono, direccion, correo, Contraseña, identificacion, tipo de usuario  |
| Fuente                 | Usuario                                 |
| Salida                 | Mensaje al correo validando que se inicio sesion correctamente |
| Destino                | pagina principal                        |
| Restricciones          | dos o mas usuarios no pueden utilixar el mismo correo | 
| Efecto colateral       |                                         | 

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
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            |permite al usuario agregar productos al carrito y apartar un producto sin la nesecidad de llevarselo enseguida |
| Entrada                | codigo del producto                     |
| Fuente                 | base de datos                           |
| Salida                 | Mansaje de producto agregado al carrito |
| Destino                | carrito con la informacion de los productos agregados (nombredelProducto, descipcion, foto, cantidad, precio, codigodeproducto, fecha)       |
| Restricciones          | Cada usuario solo puede apartar 3 productos diferes al  mismo tiempo | 
| Efecto colateral       | Esto hara que los usuarios tengan mayor tranquiliada de que un producto se les vaya terminar o escasear |

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Inica seccion                                                                             |
|- se verifica que el inicio de seccion este correcto                                        |
|- escoge el producto a comprar                                                              |
|- Ingresa producto al carrito                                                               |       
|- hace un apartado del producto a comprar determinando la fecha que vendra por este. (Opcional )   |

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
