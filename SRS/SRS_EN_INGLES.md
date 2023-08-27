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

|code                    | RF001                                   |
|------------------------|-----------------------------------------|
| Name                   | Inventory Record                        |
| Date                   | 04/27/2023                              |
| Degree of need         | High                                    |
| Description            | You must allow the administrator to show the products and the quantity with which you have each of these |
| Input                  | Gmail, Password                         |
| Source                 | Administrator                           |
| Departure              | inventory header                        |
| Destination            | Register with the available quantity of each product |
| Restriction            | Only administrative staff with a valid username can enter and view said information |
| Side effect            | This gives the administrator a better management of all his products, giving him greater efficiency when it comes to keeping track of all the products that enter and leave the company and the profits that they leave |

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- The system validates that the account has an administrator role                           |
|- The system displays the main_admin                                                        |
|- The system displays the icon to manage inventory                                          |
|- The administrator enters to manage the inventory                                          |


|Code                    | RF002                                   |
|------------------------|-----------------------------------------|
| Name                   | login                                   |
| Date                   | 04 / 07 / 2023                          |
| Degree of need         | High                                    |
| Description            | You must allow the user to log in with a type of user either (Administrator, employee or client) |
| Input                  | user type, identification and password  |
| Source                 | User                                    |
| Departure              | Message to the email validating that the session was started correctly |
| Destination            | main page                               |
| Restriction            | two or more users cannot use the same identification |
| Side effect            | main page would not be displayed        |

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Enter the main                                                                            |
|- The system loads by default the main-client                                               |
|- Enter the icon to start section                                                           |
|- Enter email and password                                                                  |
|- performs the beginning of the section                                                     |


|Code                    | RF003                                   |
|------------------------|-----------------------------------------|
| name                   | Cart module                             |
| Date                   | 04 / 07 / 2023                          |
| Degree of need         | mean                                    |
| Description            | allows the user to add products to the cart and remove a product without the need to take it immediately |
| Input                  | button (add to cart)                    |
| Source                 | database                                |
| departure              | Product message added to cart           |
| Destination            | Cart with the information of the added products (Product name, description, photo, quantity, price, product code, date) |
| restriction            | You must be registered to be able to add products to the cart |
| Side effects           | without products in the cart there will be no purchase |

| Proceso                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Enter the main                                                                            |
|- By default loads the main-client                                                          |
|- select products to add to cart                                                            |
|- The system validates that the client is logged in                                         |
|- if not, the system requests that you log in                                               |
|- If it is, the system adds the products to the cart                                        |


|Code                    | RF004                                   |
|------------------------|-----------------------------------------|
| Name                   | User registration                       |
| Date                   | Does not register                       |
| Degree of need         | High                                    |
| Description            | allows the user to register in the system, as type account (user) |
| Input                  | name, surname, identification, address, email, password |
| Source                 | user                                    |
| Departure              | successful registration message         |
| Destination            | payment method module                   |
| Restriction            | there should not be two accounts with the same email |
| Side effect            | no type of purchase could be carried out |

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Enter the main                                                                            |
|- The system loads by default the main-client                                               |
|- Enter the register icon                                                                   |
|- enter the information requested by the system                                             |
|- register                                                                                  |


|Code                    | RF005                                   |
|------------------------|-----------------------------------------|
| Name                   | buy products                            |
| Date                   | 04 / 07 / 2023                          |
| Degree of need         | High                                    |
| Description            |allows the user to make a purchase       |
| Input                  | address, payment method                 |
| Source                 | user                                    |
| Departure              | message via gmail                       |
| Destination            | cart module                             |
| Restriction            | It is mandatory to select a payment method |
| Side effect            | no type of purchase could be made       |

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- Validates that there are products in the cart                                             |
|- The system will ask for some information                                                  |
|- finalize the purchase                                                                     |


|Code                    | RF006                                   |
|------------------------|-----------------------------------------|
| Name                   | Products module                         |
| Date                   | 04 / 07 / 2023                          |
| Degree of need         | High                                    |
| Description            | details of each product for your organization |
| Input                  | name, Code, Quantity                    |
| Source                 | Employee                                |
| Departure              | Product added                           |
| Destination            | Inventory (name, Code, Quantity)        |
| Restriction            | Only employees/administrator can enter this requirement |
| Side effect            | NO Enter the product data to the inventory and Request the data again |

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- The system validates that the account has an employee role                                |
|- The system displays the main-employee                                                     |
|- The system displays the icon to manage products                                           |
|- The employee enters to manage the products (add-modify-eliminate)                         |


|Code                    | RF007                                   |
|------------------------|-----------------------------------------|
| Name                   | main                                    |
| Date                   | 04 / 07 / 2023                          |
| Degree of need         | High                                    |
| Description            | In this requirement, the main page to which users will access after logging in will be organized |
| Input                  | login                                   |
| Source                 | database                                |
| Departure              | Gmail Message                           |
| Destination            | main                                    |
| Restriction            | You have to be logged in to access this section |
| Side effect            | directs the client to log in to their account or to register | 

| Process                                                                                    | 
|--------------------------------------------------------------------------------------------|
|- When accessing the url of the page you will be directed to the main                       |
|- The system will load by default the main-Client                                           |
|- When starting the section as admin                                                        |
|- The system will load the main-admin                                                       |
|- When starting the section as an employee                                                  |
|- The system will load the main-employee                                                    |

 
## 3.2 non-functional requirements

| code       | name                      | date        | degree of need |
|------------|---------------------------|-------------|----------------|
| RNF001     | program performance       | 25/07/2023  | high           |
|description | The program must have the best performance, the best loading speed and the best possible performance to give good satisfaction to each of the users |


| code       | name                      | date        | degree of need |
|------------|---------------------------|-------------|----------------|
| RNF002     | information protection    | 25/07/2023  | high           |
|description | The program to guarantee the security of the information that users enter |


| code       | name                        | date        | degree of need |
|------------|-----------------------------|-------------|----------------|
| RNF003     | program sustainability      | 25/07/2023  | high           |
|description | The program must have the ability to remain active and working at 100%, if it presents a failure it must be able to recover in the shortest possible time without affecting the user in any way|

| code       | name                      | date        | degree of need |
|------------|---------------------------|-------------|----------------|
| RNF004     | Usability                 | 25/07/2023  | half           |
|description | The interface of the program should be as clear and simple as possible so that users can use it in the best possible way|

| code       | name                      | date        | degree of need |
|------------|---------------------------|-------------|----------------|
| RNF005     | effectiveness             | 25/072023   | high           |
|description | The program to provide the best efficiency for greater satisfaction and for a better experience on the part of users|

| code       | name                      | date        | degree of need |
|------------|---------------------------|-------------|----------------|
| RNF006     | restrictions              | 25/072023   | half           |
|description | The program must have certain restrictions depending on the role with which the program is being executed |

## 3.3 user interface requirements 

| code        | name                | date            |degree of need  |
|-------------|---------------------|-----------------|----------------|
| PF006       | Record Store        | does not record | high           |
| description | will allow to save the user's information when registering in the system |

| code        | name           | date              | degree of need |
|-------------|----------------|-------------------|----------------|
| PF007       | income and use | Does not register | High           |
| description | the program must be easy to access and use for users |


| code        | name               | date            | degree of need |
|-------------|--------------------|-----------------|----------------|
| PF008       | order registration | does not record | high           |
| description | A record will be kept of each of the orders that are made |

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