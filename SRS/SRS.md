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
| Nombre                 | Gestion de productos                    |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | El Software debe permitir al empresario mostrar los productos y la cantidad con la que dispone de cada uno de estos |
| Entrada                | Usuario                                 |
| Fuente                 | Propietario de la empresa               |
| Salida                 | Cantidad disponible de cada producto    |
| Destino                | Usuario que ingreso                     |
| Restricciones          | Solo el personal que cuente con ususario valido puede ingresar y visualizar  dicha informacion | 
| Efecto colateral       | Esto le brinda al empresario un mejor manejo de todos sus productos dándole mayor eficiencia a la hora de llevar un conteo de todo los productos que entran y salen de la empresa y las ganancias que estos dejan | 

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- ingresa usuario                                                                           |
|- verifica que el ususario sea correcto                                                     |
|- si el ususario es incorrecto vuelve a pedirlo                                             |
|- si es usuario es correcto ingresa                                                         |
|- muestra un regitro de todos los productos con la cantidad disponible de cada uno de estos |

|Codigo                  | PF002                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Gestion de pedidos rapidos              |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | Debe permitir que el usuario pueda hacer una compra rapida |
| Entrada                | Inicio de seccion                       |
| Fuente                 | Ultimo usuario                          |
| Salida                 | Productos que la empresa ofrece         |
| Destino                | Encargado de la programa                |
| Restricciones          | Si el usuario no se registra no podra hacer su compra | 
| Efecto colateral       | Esto facilitara las compras de los usuarios y haciendo que estas sean mas rapidas e eficientes | 

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Registrarse en el sistema                                                                 |
|- Omitir el regitro si ya se encuentra en el sistema                                        |
|- Inicia seccion                                                                            |
|- Verificar que se inicie seccion correctamente                                             |
|- Visualiza los priductos y escoge el producto a comprar                                    |
|- Finaliza la compra                                                                        |

|Codigo                  | PF003                                   |
|------------------------|-----------------------------------------|
| Nombre                 | Encargo o apartado de productos         |
| Fecha                  | No registra                             |
| Grado de nesecidad     | Alto                                    |
| Descripcion            | El sistema debe permitir al usuario apartar un producto sin la nesecidad de llevarselo enseguida |
| Entrada                | Inicio de seccion                       |
| Fuente                 | Ultimo usuario                          |
| Salida                 | Pedido apartado                         |
| Destino                | Encargado del programa                  |
| Restricciones          | Cada usuario solo puede apartar 3 productos diferes al  mismo tiempo | 
| Efecto colateral       | Esto hara que los usuarios tengan mayor tranquiliada de que un prosucto se les vaya terminar o escasear |

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Inica seccion                                                                             |
|- se verifica que el inicio de seccion este correcto                                        |
|- escoge el producto a comprar                                                              |
|- hace un apartado del producto a comprar determinando la fecha que vendra por este         |

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
|codigo      | nombre         | fecha   |grado necesida |
|------------|----------------|---------|---------------|
|            |                |         |               |
|descripcion |                                          |


|codigo      | nombre         | fecha   |grado necesida |
|------------|----------------|---------|---------------|
|            |                |         |               |
|descripcion |                                          |


|codigo      | nombre         | fecha   |grado necesida |
|------------|----------------|---------|---------------|
|            |                |         |               |
|descripcion |                                          |
