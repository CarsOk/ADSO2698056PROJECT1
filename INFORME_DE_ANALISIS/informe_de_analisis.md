
#  <h1><center>**SENA**</center></h1>

## <h2>SERVICIO NACIONAL DE APRENDISAJE </h2>
(CENTRO INDUSTRIAL Y DE AVIACION)

INFORME DE ANALISIS <br>
Presentado por:<br>
Juan David Sarmiento Dìaz <br>
Katryn Johana González Rodríguez<br>
Geronimo jose castillo martinez<br>
Thomas David Güette Marriaga<br>
Maiyer David Hernández Nietoa<br>

**<center>HISTORIAL DE REVISIONES</center>**
|fecha | versiòn | descripciòn/cambio | autor|
|------|---------|--------------------|------|
|07/07/2023 <br> 25/07/2023|1.0 <br> 1.1| Primer documento. <br> actualizaciòn de documento.| Juan David Sarmiento Dìaz. <br> Katryn Johana González Rodríguez. <br> Geronimo jose castillo martinez. <br> Thomas David Güette Marriaga. <br> Maiyer David Hernández Nieto.

1. **PROPOSITO.** <br>

El propósito de este documento de análisis es dar a conocer los requerimientos
funcionales con sus estructuras para que puedan ser utilizadas en la fase de diseño
del proyecto formativo.

2. **ALCANCE.** <br>

Realizaremos una tienda web con inventario, que permitirá llevar a cabo el control
sobre la entrada y salida de los productos que se registran en la farmacia (famisalud
la 91), se llevará a cabo la venta de estos mismos todo esto con el fin de poder
mejorar las ventas y la organización, en este proyecto no realizaremos la instalación
ni haremos el mantenimiento del software.

3. **DEFINICIONES, ACRONIMOS Y ABREVIATURAS** <br>

**SENA:** Servicio Nacional de Aprendizaje. <br>

**Web:** Un sitio web, portal o cibersitio es una colección de páginas web relacionadas y comunes a un dominio de internet o subdominio en la World Wide Web dentro de Internet. <br>

**Sofía:** Sistema Optimizado para la Formación Integral del Aprendizaje Activo. <br>

**Base de datos:** una base de datos se encarga no solo de almacenar datos, sino también de conectarlos entre sí en una unidad lógica. <br>

**Software:** Estos son los programas informáticos que hacen posible la ejecución de
tareas específicas dentro de un computador. Por ejemplo, los sistemas operativos, aplicaciones, navegadores web, juegos o programas. <br>

**inventario:** El inventario es la comprobación manual de que las cantidades físicas y reales en stock de cada producto de nuestra farmacia coinciden con las cantidades
de cada producto registrados en el programa informático de gestión. <br>

**Firewall:** es un sistema de seguridad de red de las computadoras que restringe el tráfico de Internet entrante, destaca o dentro de una red privada. <br>

**Requerimientos funcionales:** descripción de las capacidades o funciones que el sistema será capaz de realizar. <br>

**Requerimientos no funcionales:** restricciones o características que delimitan el sistema, como, por ejemplo, rendimiento, interfaces de usuario, confiabilidad, seguridad, portabilidad, normas, entre otros. <br>

4. **PERSONAL.** <br>

|**NOMBRE**|**CORREO**|**TELEFONO**|
|----------|----------|------------|
|Katryn Johana gonzálezRodríguez |katrinjhoanagonzalezrodriguez@gmail.com|3022349798|
|Geronimo jose castillo martinez |jeromartinezcas21@gmail.com|3206926305|
|Thomas David Güette Marriaga|thomasmarriaga487@gmail.com|3003687800|
|Maiyer David Hernández Nieto|maiyerhernandezn@gmail.com|3046722344|
|Juan David Sarmiento Díaz|jjuandsarmiento04@gmail.com|3042285552|

5. **SITUCACION ACTUAL.** <br>

La empresa Famisalud 91 en la actualidad esta administrada por Duvis González quien es la propietaria del negocio, la cual maneja la empresa con la ayuda de su esposo quienes son los únicos que administran el negocio. <br>

La empresa no cuenta con ningún tipo de software que ayude a facilitar, mejora y dar mayor eficacia al manejo de la empresa, lo que lleva a dar déficit en varias áreas de esta. <br>

Unas de las áreas que puede presentar déficit puede ser el área de inventario debido a que los productos de entrada y salida son registrados.<br>
manualmente en libretas u otras herramientas y esto puede llevar a la perdida de información, En el área de contabilidad se presentan dificultades
a la hora del manejo de las cuentas debido a que se hace manualmente esto puede llevar a ineficacia a la hora de llevar la contabilidad de la empresa. 

Debido a las dificultades que viene presentando la farmacia famisalud la 91 surge la necesidad de diseñar una tienda web para esta que ayude a mejorar algunos de los problemas que la empresa presenta. Con este software se busca disminuir, cambiar o minimizar lo más posible las problemáticas que vienen presentando la empresa, haciendo que esta tenga una mayor eficacia en la mayor parte de sus áreas, facilitando el trabajo y mejorando las ventas. <br>

6. **PERSPECTIVA DEL PRODUCTO.** <br>

De este software se espera tener una mejora en el área de las ventas y la administración de la empresa. Se busca facilitar el trabajo administrativo sin disminuir las ventas y brindando una mayor eficacia. <br>

Lo que llevara al aumento de los clientes y mayor ingreso monetario al
negocio. <br>

El inventario hará que se lleve de mejor manera la información de los productos de entrada y salida, previniendo la perdida de información. <br>

7. **FUNCIONES DEL PRODUCTO.** <br>

 Registro de Inventario <br>
 inicio de sesión <br>
 Módulo de carrito <br>
 registro de usuario <br>
 modulo método de pago <br>
 módulo de productos <br>
 Modulo principal <br>

8. **CARACTERISTICAS DE USUARIO.** <br>

Los usuarios serán los clientes, los empleados y los administradores. <br>

Los clientes tendrán acceso a la visualización y compra de los productos que se encuentran disponibles. <br>

Los empleados tienen acceso al registro de los productos que ingresan y salen de la farmacia y al apartado de los pedidos y las ventas realizadas en físico. <br>

El administrador tendrá acceso a las ventas y al registro de los productos. <br>

9. **REQUERIMIENTOS FUNCIONALES.** <br>

|CODIGO|NOMBRE|
|------|------|
|RF-001|Registro de Inventario|
|ALTO|Debe permitir al administrador mostrar los productos y la cantidadcon la que dispone de cada uno de estos|
|RF-002|inicio de sesión|
|ALTO|Debe permitir al usuario iniciar sesión con un tipo de usuario ya sea(Administrador, empleado o cliente) |
|RF-003|Módulo de carrito|
|MEDIO|permite al usuario agregar productos al carrito y apartar un productosin la necesidad de llevárselo enseguida|
|RF-004|registro de usuario|
|ALTO|permite al usuario registrase en el sistema, como cuenta tipo(usuario)|
|RF-005|modulo método de pago|
|ALTO|permite al usuario seleccionar la forma de pago del producto|
|RF-006|módulo de productos |
|ALTO|detalles de cada producto para su organización|
|RF-007|Modulo principa|
|ALTO|En este requerimiento se va a organizar la página principal a la cual van a acceder los usuarios después de iniciar sesión|



10. **REQUERIMIENTOS NO FUNCIONALES** <br>

|CODIGO|NOMBRE|
|------|------|
|RNF-001|Rendimiento del programa |
|ALTO|El programa debe tener el mejor rendimiento, la mejor velocidad de carga y el mejor desempeño posible para dar una buena satisfacción a cada uno de lo usuarios |
|RNF-002|Protección de información |
|ALTO|El programa debe garantizar la seguridad de la información que los usuarios ingresan|
|RNF-003|Sostenibilidad del programa|
|ALTO|El programa debe tener la capacidad de mantenerse activo y funcionando a su 100% si llega a presentar alguna falla debe ser capaz de recuperarse en el menos tiempo posible sin afectar de ninguna forma a los usuarios |
|RNF-004|Usabilidad |
|ALTO|La interfaz del programa debe ser lo más clara y sencilla posible para que a los usuarios se le facilite su manejo de la mejor manera|
|RNF-005|Eficacia |
|ALTO|El programa de brindar la mejor eficacia para mayor satisfacción y para una mejor experiencia de parte de los usuarios|
|RNF-006|Restricciones |
|ALTO|El programa debe tener ciertas restricciones dependiendo del rol con el que se esté acabó el programa|

11. **MODELO ENTIDAD RELACION** <br>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image.png?raw=true" width ="800" height="550"/>

12. **DIAGRAMA CASOS DE USO (UML)** <br>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-1.png?raw=true" width ="800" height="550"/>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-2.png?raw=true" width ="800" height="550"/>


<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>INICIAR SESION</center>
        </th>
    </tr>
    <tr>
        <td>
            <b> <center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El comportamiento del sistema deberá describir el paso a paso cuando el usuario vaya a iniciar sección.
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El usuario debe estar registrado para poder iniciar sección
        </td>
    </tr>
    <tr>
        <td rowspan="6">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Ingresa al main
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            el sistema carga por predeterminado el main-cliente
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            Ingresa al icono iniciar sección
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            Ingresa el correo y la contraseña 
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            No se valida el inicio de sección
        </td>
    </tr>
    <tr>
        <td rowspan = "3">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Si no se encuentra registrado no podrá iniciar sesión 
        </td>
    </tr>
</table>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-4.png?raw=true" width ="800" height="550"/>

<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>REGISTRO USUARIO</center>
        </th>
    </tr>
    <tr>
        <td>
            <b><center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El comportamiento del sistema deberá describir el paso a paso cuando el usuario vaya a registrarse.
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El usuario debe contar con los datos necesarios para registrarse
        </td>
    </tr>
    <tr>
        <td rowspan="6">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Ingresa al main
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            el sistema carga por predeterminado el main-cliente
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            Ingresa al icono registrarse
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            Ingresa la información solicitada por el sistema 
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            No se valida el registro
        </td>
    </tr>
    <tr>
        <td rowspan = "4">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            el sistema no permitirá registrarse si el correo utilizado ya se encuentra en otra cuenta existente
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            el sistema no permitirá registrarse si alguna de la información suministrada por el usuario es incorrecta o no valida
        </td>
    </tr>
</table>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-6.png?raw=true" width ="800" height="550"/>

<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>AÑADIR PRODUCTOS AL CARRITO</center>
        </th>
    </tr>
    <tr>
        <td>
            <b> <center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El sistema deberá describir el paso a paso cuando el cliente vaya a agregar un o más productos al carrito.
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El Cliente debe tener un inicio de sección activo
        </td>
    </tr>
    <tr>
        <td rowspan="7">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Ingresa al main
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            el sistema carga por predeterminado el main-cliente
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            Selecciona producto que va a agregar al carrito
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            Valida que el cliente este logueado
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>5
        </td>
        <td>
            Agrega producto al carrito
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            El cliente no tiene cuenta
        </td>
    </tr>
    <tr>
        <td rowspan = "3">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            el sistema no permitirá añadir productos al carro si el cliente no está logueado.
        </td>
    </tr>
</table>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-8.png?raw=true" width ="800" height="550"/>

<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>COMPRAR PRODUCTOS</center>
        </th>
    </tr>
    <tr>
        <td>
            <b><center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El sistema deberá describir el paso a paso cuando el usuario vaya a realizar una compra de uno o más productos
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El Cliente debe tener un inicio de sección activo
        </td>
    </tr>
    <tr>
        <td rowspan="8">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            añadir 1 o más artículos
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            solicitar la ubicación a la cual se llevaran los productos
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            solicitar el pago de los productos
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            verificar el pago realizado por el Cliente
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>5
        </td>
        <td>
            Al iniciar sección como Empleado
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>6
        </td>
        <td>
            confirmar/denegar envió al cliente
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            EL Cliente realiza el pago de los productos
        </td>
    </tr>
    <tr>
        <td rowspan = "4">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            El Sistema realizara la devolución del dinero siempre y cuando se realice una denegación del envío del pedido
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            No se realiza el pago correctamente (se notifica de que no se pudo realizar el pago y lo devuelve al main)
        </td>
    </tr>
</table>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-10.png?raw=true" width ="800" height="550"/>

<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>GESTIONAR PRODUCTOS</center>
        </th>
    </tr>
    <tr>
        <td>
            <b> <center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El sistema deberá describir el paso a paso cuando empleado vaya a gestionar los productos de la tienda.
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El empleado debe haber iniciado sección con una cuenta que tenga rol de empleado
        </td>
    </tr>
    <tr>
        <td rowspan="6">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            El sistema valida que la cuenta tenga rol empleado
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            El sistema despliega el Main-empleado
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            El sistema despliega icono de gestionar productos
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            El empleado ingresa a gestionar los productos 
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            No cuenta con una cuenta de rol empleado
        </td>
    </tr>
    <tr>
        <td rowspan = "3">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Sin el rol valido el sistema no va a desplegar el Main-empleado
        </td>
    </tr>
</table>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-12.png?raw=true" width ="800" height="550"/>

<table border ="5px">
    <tr style="color:BLACK">
        <th style="background-color: yellow">
            CASO DE USO
        </th>
        <th style="background-color: yellow" colspan="2">
            <center>ADMINISTRAR INVENTARIO</center>
        </th>
    </tr>
    <tr>
        <td>
            <b> <center>DESCRIPCION</center>
        </td>
        <td colspan="2">
            El sistema deberá describir el paso a paso cuando el administrador vaya a administrar el inventario.
        </td>
    </tr>
    <tr>
        <td>
            <B><center>PRECONDICION</center>
        </td>
        <td colspan="2">
            El administrador debe haber iniciado sección con una cuenta que tenga rol de administrador
        </td>
    </tr>
    <tr>
        <td rowspan="6">
            <B><center>SECUENCIA NORMAL</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            El sistema valida que la cuenta tenga rol administrador
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>2
        </td>
        <td>
            El sistema despliega el Main-administrador
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>3
        </td>
        <td>
            El sistema despliega icono de administrar inventario
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>4
        </td>
        <td>
            El administrador ingresa a administrar inventario
        </td>
    </tr>
    <tr>
        <td>
            <b><center>POSTCONDICION</center>
        </td>
        <td colspan="2">
            No cuenta con una cuenta de rol administrador
        </td>
    </tr>
    <tr>
        <td rowspan = "3">
            <b><center>EXCEPCIONES</center>
        </td>
    </tr>
    <tr style="color:BLACK">
        <td style="background-color: yellow">
            <B>PASO
        </td>
        <td style="background-color: yellow">
            <B><center>ACCION</center>
        </td>
    </tr>
    <tr>
        <td style="color:yellow">
            <b>1
        </td>
        <td>
            Si no cuenta con el rol permitido no podrá administrar el inventario 
        </td>
    </tr>
</table>

13. **DIAGRAMA DE ACTIVIDADES (UML)** <br>

<center>Agregar productos al carrito</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-19.png?raw=true" width ="600" height="350"/>

<center>Registrar Usuario</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-18.png?raw=true" width ="600" height="350"/>

<center>Iniciar sesión</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-17.png?raw=true" width ="600" height="350"/>

<center>Administrar inventario</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-16.png?raw=true" width ="600" height="450"/>

<center>Comprar productos</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-15.png?raw=true" width ="500" height="450"/>

<center>Gestionar productos</center>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-14.png?raw=true" width ="600" height="350"/>

14. **DIAGRAMA DE CLASES (UML)** <br>

<img src= "https://github.com/CarsOk/ADSO2698056PROJECT1/blob/main/INFORME_DE_ANALISIS/IMAGENES/image-20.png?raw=true" width ="800" height="550"/>