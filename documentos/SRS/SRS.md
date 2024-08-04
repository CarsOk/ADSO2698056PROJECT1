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

<style>
        table, th, td{
            border: 1px solid black;
            border-collapse: collapse;
            
        }
</style>
<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-001</td>
            <td colspan="2">Registro de Inventario</td>
            <td>04/ 27 / 2023</td>
            <td>ALTO</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">Debe permitir al administrador mostrar los productos y la cantidad con la que dispone de cada uno de estos</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>Gmail, Contraseña</td>
            <td>Administrador</td>
            <td>emcabezado de inventario</td>
            <td>Regitro con la cantidad disponible de cada producto</td>
            <td>Solo el personal administrativo que cuente con ususario valido puede ingresar y visualizar dicha informacion</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>El sistema valida que la cuenta tenga rol administrador.</li>
                    <li>El sistema despliega el main_admin.</li>
                    <li>El sistema despliega el icono de administrar inventario.</li>
                    <li>El administrador ingresa a administrar el inventario.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">Esto le brinda al administrador un mejor manejo de todos sus productos dándole mayor eficiencia a la hora de llevar un conteo de todo los productos que entran y salen de la empresa y las ganancias que estos dejan</td>
        </tr>
</table>

<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-002</td>
            <td colspan="2">Inicio de sesion</td>
            <td>04 / 07 / 2023</td>
            <td>ALTO</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">Debe permitir al usuario iniciar sesion con un tipo de usuario ya sea (Administrador, empleado o cliente)</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>tipo de ususario, identificacion y contraseña</td>
            <td>usuario</td>
            <td>Mensaje al correo validando que se inicio sesion correctamente</td>
            <td>pagina principal</td>
            <td>dos o mas usuarios no pueden utilizar la misma identificacion</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>Ingresa al main</li>
                    <li>El sistema carga por predeterminado el main-cliente</li>
                    <li>Ingresa al icono de iniciar seccion</li>
                    <li>Ingresa el correo y la contraseña</li>
                    <li>realiza el inicio de seccion</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">no se desplegaria pagina principal</td>
        </tr>
</table>


<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-003</td>
            <td colspan="2">Modulo de carrito</td>
            <td>04 / 07 / 2023</td>
            <td>Media</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">permite al usuario agregar productos al carrito y apartar un producto sin la nesecidad de llevarselo enseguida</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>boton (agregar al carrito)</td>
            <td>base de datos</td>
            <td>Mansaje de producto agregado al carrito</td>
            <td>carrito con la informacion de los productos agregados (nombre del Producto, descripcion, foto, cantidad, precio, codigo deproducto, fecha)</td>
            <td>debe de estar registrado para poder agregar productos al carrito</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>Ingresa al main</li>
                    <li>por predeterminado el main-cliente</li>
                    <li>seleciona productos que va a agregar al carrito</li>
                    <li>El sistema valida que el cliente este logeado</li>
                    <li>En caso de no estarlo el sistema solicita que se logee</li>
                    <li>En caso de si estarlo el sistema agrega los productos al carrito</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">sin productos en el carrito no habra compra</td>
        </tr>
</table>

<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-004</td>
            <td colspan="2">Registro de usuario</td>
            <td>No registra</td>
            <td>Alto</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">permite al usuario registrase en el sistema, como cuenta tipo (usuario)</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>nombre, apellidos, identificacion, direccion, correo, contraseña</td>
            <td>usuario</td>
            <td>mensaje de registro exitoso</td>
            <td>modulo metodo de pago</td>
            <td>no debe haber dos cuentas con el mismo correo</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>Ingresa al main</li>
                    <li>El sistema carga por predeterminado el main-cliente</li>
                    <li>Ingresa al icono registrarse</li>
                    <li>ingresa la informacion solicitada por el sistema</li>
                    <li>realiza el registro</li>
                </ul>    
            </td>
        </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">no se podria llevar a cabo ningun tipo de compra</td>
        </tr>
</table>


<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-005</td>
            <td colspan="2">Comprar productos</td>
            <td>04 / 07 / 2023</td>
            <td>Alto</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">permite al usuario realizar una compra</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>direccion, forma de pago</td>
            <td>usuario</td>
            <td>mensaje via gmail</td>
            <td>modulo del carrito</td>
            <td>es obligario seleccionar un metodo de pago</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li> Valida que haya productos en el carrito</li>
                    <li>El sistema le pedira unos datos</li>
                    <li>finaliza la compra</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">no se podria realizar ningun tipo de compra</td>
        </tr>
</table>

<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-006</td>
            <td colspan="2">Modulo de productos</td>
            <td>04/ 07/ 2023</td>
            <td>Alto</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">detalles de cada producto para su organizacion</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>nombre, Codigo, Cantidad</td>
            <td>Empleado</td>
            <td>Producto añadido</td>
            <td>Inventario (nombre, Codigo, Cantidad)</td>
            <td>Solo los empleados/administrador Pueden Ingresar a este requerimiento</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>El sistema valida que la cuenta tenga rol empleado</li>
                    <li>El sistema despliega el main-empleado</li>
                    <li>El sistema despliega icono de gestionar productos</li>
                    <li>El empleado ingresa a gestionar los preductos (agregar-modificar-eliminar)</li>
                </ul>    
            </td>
        </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">NO Ingresar Los datos de producto al inventario y Solicitar los datos nuevamente</td>
        </tr>
</table>       

<table style="width: 90%;">
        <tr>
            <th>Codigo</th>
            <th colspan = "2">Nombre</th>
            <th>Fecha</th>
            <th>Grado de necesidad</th>
        </tr> 
        <tr align="center">
            <td>RF-007</td>
            <td colspan="2">Registro de usuario</td>
            <td>04 / 07 / 2023</td>
            <td>Alto</td>
        </tr>
        <tr align="center">
            <td>Descripción</td>
            <td colspan ="4">en este requerimiento se va a organizar la pagina principal a la cual se van a acceder los usuarios despues de iniciar sesion</td>
        </tr>
        <tr align="center">
            <th>Entradas</th>
            <th>Fuente</th>
            <th>Salida</th>
            <th>Destino</th>
            <th>Restricciones</th>
        </tr>
        <tr align="center">
            <td>inicio de sesion</td>
            <td>Fuente	base de datos</td>
            <td>Salida	Mensaje Gmail</td>
            <td>Destino	main</td>
            <td>Restriccion	tiene que estar logueado para poder acceder a este apartado</td>
        </tr>
        <tr>
            <td>Proceso</td>
            <td colspan = "4">
                <ul>
                    <li>Al acceder a la url del la pagina sera direccionado/a al main</li>
                    <li>El sistema cargar por predeterminado el main-Cliente</li>
                    <li>Al iniciar seccion como admin</li>
                    <li>El sistema cargara el main-admin</li>
                    <li>Al iniciar seccion como empleado</li>
                    <li>El sistema cargara el main-empleado</li>
                </ul>    
            </td>
        </tr>
        <tr align="center">
            <td>Efecto colateral</td>
            <td colspan="4">manda al cliente a iniciar sesion en su cuenta o a que se registre</td>
        </tr>
</table>

## 3.2 resquerimirntos no funcionales 
<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF001 </td>
            <td rowspan=1 align="center">Rendimiento del programa</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">El programa debe tener el mejor rendimiento, la mejor velocidad de carga y el mejor desenpeño posible para dar una buena satisfaccion a cada uno de los usuarios</td>
        </tr>
        </tr>  
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF002 </td>
            <td rowspan=1 align="center"> proteccion de informcion </td>
	    <td rowspan=1 align="center">25/072023  </td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center"> El programa de garantizar la seguridad de la informcion que los usuarios ingresan</td>
        </tr>
        </tr>  
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF003 </td>
            <td rowspan=1 align="center">sostenibilidad del programa</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">El programa debe tener la capacidad de mantenerse activo y funcionando a su 100%, si llega a presentar algun fallo debe ser capaz de recuperarse en el menor tiempo posible sin afectar de ninguna forma al usuario</td>
        </tr>
        </tr>  
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF004 </td>
            <td rowspan=1 align="center">Usabilidad</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">Medio</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center"> La interfaz del programa debe ser lo mas clara y sencilla posible para que a los usuarios se le facilite su manejo de la mejor manera</td>
        </tr>
        </tr>  
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF005 </td>
            <td rowspan=1 align="center">eficacia</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">El programa de brindar la mejor eficacia para mayor satisfacción y para una mejor experiencia de parte de los usuarios</td>
        </tr>
        </tr>  
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF006 </td>
            <td rowspan=1 align="center">Restricciones</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">El programa debe tener ciertas restricciones dependiendo el rol con el que se este ejecutando el programa 
</td>
        </tr>
        </tr>  
    </tbody>
</table>

 
## 3.3 requerimientos de interfaz de usuario 
<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF006</td>
            <td rowspan=1 align="center">Almacen de registro</td>
	    <td rowspan=1 align="center">No registra</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">permitira guardar la informcaion del ususario al regitrarse en el sistema</td>
        </tr>
        </tr>  
    </tbody>
</table>



<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF007</td>
            <td rowspan=1 align="center">ingreso y uso</td>
	    <td rowspan=1 align="center">No registra</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">el programa debe terner un acceso y un uso facil para los usuarios</td>
        </tr>
        </tr>  
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>codigo</th>
            <th>nombre</th>
            <th>fecha</th>
	     <th>grado necesida</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF008</td>
            <td rowspan=1 align="center">registro de pedido</td>
	    <td rowspan=1 align="center">No registra</td>
            <td rowspan=1 align="center">Alto</td>
        </tr>
        <tr>
            <th align="center">descripcion</th>
	    <td colspan="3" align="center">Se guardara un registro de cada uno de los pedidos que se hagan</td>
        </tr>
        </tr>  
    </tbody>
</table>


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
