# 1.	introduction

ANALYSIS, DESIGN, DEVELOPMENT AND IMPLEMENTATION OF A WEB APPLICATION IN THE PHARMACY (Famisalud La 91) FOR THE ORGANIZATION AND VIRTUAL SALE OF A PHARMACY.

## 1.1	Purpose

The purpose of this is to describe what was agreed with the client and create step by step the software that will be used to carry out the inventory and sale of the products that the pharmacy offers, by systematizing these processes we will have a better performance in the inventory area and sale.

## 1.2	scope

We will make a virtual store with inventory, which will allow us to control the entry and exit of the products that are registered in the pharmacy (famisalud la 91), the sale of these will be carried out, all this in order to improve the sales and organization, in this project we will not perform the installation or maintenance of the software.

## 1.3	define, acronym and abbreviation

SENA: National Learning Service.

Sofia: Optimized System for the Comprehensive Training of Active Learning.

Database: a database is responsible not only for storing data, but also for connecting them together in a logical unit.

Software: These are the computer programs that make it possible to execute specific tasks within a computer. For example, operating systems, applications, web browsers, games or programs.

Inventory: Inventory is the manual verification that the physical and real quantities in stock of each product in our pharmacy coincide with the quantities of each product registered in the management computer program.

Firewall: is a computer network security system that restricts Internet traffic incoming, outgoing, or within a private network.

Functional requirements: describe the capabilities or functions that the system will be able to perform.

Non-functional requirements: restrictions or characteristics that define the system, such as performance, user interfaces, reliability, security, portability, standards, among others.

## 1.4	reference

https://edu.gcfglobal.org/es/informatica-basica/que-es-hardware-y-software/1/

https://www.arimetrics.com/glosario-digital/base-de-datos

https://www.mcafee.com/es-co/antivirus/firewall.html

http://www.pmoinformatica.com/2018/05/que-es-requerimiento-funcional.html

https://visuresolutions.com/es/blog/non-functional-requirements/

## 1.5	 overall appreciation

A short introduction is presented in this document.
Where in the next part you can see the perspective of the project, with its functions, specifications and characteristics of the project itself and its future users.
Point 3 presents a detailed specification of the requirements that are necessary for the analysis, design, development and implementation of the system.


# 2.	General description

## 2.1	Product Insights

-  With this software, an improvement is expected in the way part of the sale and part of the inventory are handled in the famisalud la 91 pharmacy.
- Said inventory will be the best way to keep the information of the sales and the registration of the products.
 
## 2.2	Product Features

- Register client.
- Register product.
- Register purchase details.
- Register income products.
- Register output products.
- Register order details.
- Visualization of available products.
- Generate report of scarce products.

## 2.3	User Features

- The users will be the clients, the employees and the administrators.
- Customers are given access to view and purchase the products that are available.
- Employees will have access to the record of products that enter and leave the pharmacy and to the section of orders and sales made in physical.
- The administrator will have access to sales and product registration.

## 2.4	restrictions

- For this system, the possible restrictions are the time it will take to develop it, resources where the system will be implemented, the level of programming language for developers.

## 2.5	Attention and Dependencies

- The system will keep track of sales, inventory, order registration and customer registration.
	
# 3.	Specific requirements

## 3.1	Functional Requirements

<style>
        table, th, td{
            border: 1px solid black;
            border-collapse: collapse;
            
        }
</style>
<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-001</td>
            <td colspan="2">Inventory Record</td>
            <td>04/ 27 / 2023</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">You must allow the administrator to show the products and the quantity with which you have each of these.</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>Gmail, Password.</td>
            <td>Administrator.</td>
            <td>inventory header.</td>
            <td>Register with the available quantity of each product.</td>
            <td>Only administrative staff with a valid username can enter and view said information.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>The system validates that the account has an administrator role.</li>
                    <li>The system displays the main_admin.</li>
                    <li>The system displays the icon to manage inventory.</li>
                    <li>The administrator enters to manage the inventory.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">This gives the administrator a better management of all his products, giving him greater efficiency when it comes to keeping track of all the products that enter and leave the company and the profits that they leave.</td>
        </tr>
</table>





<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-002</td>
            <td colspan="2">login</td>
            <td>04/ 27 / 2023</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">You must allow the user to log in with a type of user either (Administrator, employee or client).</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>user type, identification and password.</td>
            <td>User.</td>
            <td>Message to the email validating that the session was started correctly.</td>
            <td>main page.</td>
            <td>two or more users cannot use the same identification.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>Enter the main.</li>
                    <li>The system loads by default the main-client.</li>
                    <li>Enter the icon to start section.</li>
                    <li>Enter email and password.</li>
                    <li>performs the beginning of the section.</li>  
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">performs the beginning of the section.</td>
        </tr>
</table>




<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-003</td>
            <td colspan="2">performs the beginning of the section</td>
            <td>04/ 27 / 2023</td>
            <td>mean</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">allows the user to add products to the cart and remove a product without the need to take it immediately.</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>button (add to cart).</td>
            <td>database</td>
            <td>Product message added to cart.</td>
            <td>Cart with the information of the added products (Product name, description, photo, quantity, price, product code, date).</td>
            <td>You must be registered to be able to add products to the cart.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>Enter the main.</li>
                    <li>By default loads the main-client.</li>
                    <li>select products to add to cart.</li>
                    <li>The system validates that the client is logged in.</li>
                    <li>if not, the system requests that you log in.</li>
                    <li>If it is, the system adds the products to the cart.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">without products in the cart there will be no purchase.</td>
        </tr>
</table>




<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-004</td>
            <td colspan="2">User registration</td>
            <td>Does not register</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">allows the user to register in the system, as type account (user).</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>name, surname, identification, address, email, password.</td>
            <td>user.</td>
            <td>successful registration message.</td>
            <td>payment method module.</td>
            <td>there should not be two accounts with the same email.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>Enter the main.</li>
                    <li>The system loads by default the main-client.</li>
                    <li>Enter the register icon.</li>
                    <li>enter the information requested by the system.</li>
                    <li>register.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">no type of purchase could be carried out.</td>
        </tr>
</table>





<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-005</td>
            <td colspan="2">buy products</td>
            <td>04/ 27 / 2023</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">allows the user to make a purchase.</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>address, payment method.</td>
            <td>user.</td>
            <td>message via gmail.</td>
            <td>cart module.</td>
            <td>It is mandatory to select a payment method.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>Validates that there are products in the cart.</li>
                    <li>The system will ask for some information.</li>
                    <li>finalize the purchase.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">no type of purchase could be made.</td>
        </tr>
</table>



<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name</th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-006</td>
            <td colspan="2">Products module</td>
            <td>04/ 27 / 2023</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">details of each product for your organization.</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>name, Code, Quantity.</td>
            <td>Employee.</td>
            <td>Product added.</td>
            <td>Inventory (name, Code, Quantity).</td>
            <td>Only employees/administrator can enter this requirement.</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>The system validates that the account has an employee role.</li>
                    <li>The system displays the main-employee.</li>
                    <li>The system displays the icon to manage products.</li>
                    <li>The employee enters to manage the products (add-modify-eliminate).</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">NO Enter the product data to the inventory and Request the data again.</td>
        </tr>
</table>




<table style="width: 90%;">
        <tr>
            <th>Code</th>
            <th colspan = "2">Name </th>
            <th>Date</th>
            <th>Degree of need</th>
        </tr> 
        <tr align="center">
            <td>RF-007</td>
            <td colspan="2">Main</td>
            <td>04/ 27 / 2023</td>
            <td>High</td>
        </tr>
        <tr align="center">
            <td>Description</td>
            <td colspan ="4">In this requirement, the main page to which users will access after logging in will be organized.</td>
        </tr>
        <tr align="center">
            <th>Input</th>
            <th>Source</th>
            <th>Departure</th>
            <th>Destination</th>
            <th>Restriction</th>
        </tr>
        <tr align="center">
            <td>Login</td>
            <td>Database</td>
            <td>Gmail Message</td>
            <td>Main</td>
            <td>You have to be logged in to access this section</td>
        </tr>
        <tr>
            <td>Process</td>
            <td colspan = "4">
                <ul>
                    <li>When accessing the url of the page you will be directed to the main.</li>
                    <li>The system will load by default the main-Client.</li>
                    <li>When starting the section as admin.</li>
                    <li>The system will load the main-admin.</li>
                    <li>When starting the section as an employee.</li>
                    <li>The system will load the main-employee.</li>
                </ul>    
            </td>
            </tr>
        <tr align="center">
            <td>Side effect</td>
            <td colspan="4">directs the client to log in to their account or to register.</td>
        </tr>
</table>



 
## 3.2 non-functional requirements

<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF001 </td>
            <td rowspan=1 align="center">program performance</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The program must have the best performance, the best loading speed and the best possible performance to give good satisfaction to each of the users</td>
        </tr>
        </tr>  
    </tbody>
</table>



<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF002</td>
            <td rowspan=1 align="center">information protection</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The program to guarantee the security of the information that users enter</td>
        </tr>
        </tr>  
    </tbody>
</table>



<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF003</td>
            <td rowspan=1 align="center">program sustainability</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center"> high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The program must have the ability to remain active and working at 100%, if it presents a failure it must be able to recover in the shortest possible time without affecting the user in any way</td>
        </tr>
        </tr>  
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF004</td>
            <td rowspan=1 align="center">Usability</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">half</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The interface of the program should be as clear and simple as possible so that users can use it in the best possible way</td>
        </tr>
        </tr>  
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF005</td>
            <td rowspan=1 align="center">effectiveness</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center">high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The program to provide the best efficiency for greater satisfaction and for a better experience on the part of users</td>
        </tr>
        </tr>  
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">RNF006</td>
            <td rowspan=1 align="center">restrictions</td>
	    <td rowspan=1 align="center">25/072023</td>
            <td rowspan=1 align="center"> high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">The program must have certain restrictions depending on the role with which the program is being executed</td>
        </tr>
        </tr>  
    </tbody>
</table>


## 3.3 user interface requirements 

<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF006</td>
            <td rowspan=1 align="center">Record Store</td>
	    <td rowspan=1 align="center">does not record</td>
            <td rowspan=1 align="center"> high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">will allow to save the user's information when registering in the system </td>
        </tr>
        </tr>  
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF007</td>
            <td rowspan=1 align="center">income and use</td>
	    <td rowspan=1 align="center">does not record</td>
            <td rowspan=1 align="center"> high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">the program must be easy to access and use for users</td>
        </tr>
        </tr>  
    </tbody>
</table>



<table>
    <thead>
        <tr>
            <th>code</th>
            <th> name</th>
            <th>date</th>
	     <th>edgree of need</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=1 align="center">PF008</td>
            <td rowspan=1 align="center">order registration</td>
	    <td rowspan=1 align="center">does not record</td>
            <td rowspan=1 align="center"> high</td>
        </tr>
        <tr>
            <th align="center">description</th>
	    <td colspan="3" align="center">A record will be kept of each of the orders that are made</td>
        </tr>
        </tr>  
    </tbody>
</table>

# 4. Determination of Hardware technologies, Software and services required

## 4.1 Software

The software will be created using the programming language (Python), for this work we will use the SQLite database due to its simplicity, efficiency as well as its speed and we will use visual studio code as the main development tool.

## 4.2 Hosting

The Hosting that we will use in this work is not defined but it should be noted that the hosting service that is contracted must have sufficient storage capacity for our program.

## 4.3 Computer

To develop the software, you must have a computer regardless of the model with at least a 2.5 GHz processor and 6 cores, an 8 GB Ran and a 300 GB solid disk

## 4.4 Automatic Barcode Reader Scanner USB Support Base

It is required to use a bar reader scanner, this must have a good quality and it must be USB support

## 4.5 Router (Wireless Router/WiFi Repeater N300Mbps, Tp-Link TL-WR840N)

## 4.6 budget

Undefined
