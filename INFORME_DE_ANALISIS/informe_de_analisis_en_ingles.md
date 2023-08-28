#  <h1><center>**SENA**</center></h1>

## <h2>NATIONAL LEARNING SERVICE</h2>
(CENTRO INDUSTRIAL Y DE AVIACION)

ANALYSIS REPORT <br>
Presented by:<br>
Juan David Sarmiento Dìaz <br>
Katryn Johana González Rodríguez<br>
Geronimo jose castillo martinez<br>
Thomas David Güette Marriaga<br>
Maiyer David Hernández Nietoa<br>

**<center>REVISION HISTORY</center>**
|date  | versiòn | description/change | author|
|------|---------|--------------------|------|
|07/07/2023 <br> 25/07/2023|1.0 <br> 1.1| first document. <br> document update.| Juan David Sarmiento Dìaz. <br> Katryn Johana González Rodríguez. <br> Geronimo jose castillo martinez. <br> Thomas David Güette Marriaga. <br> Maiyer David Hernández Nietoa.

1. **PURPOSE.** <br>

The purpose of this analysis document is to present the requirements
functional with their structures so they can be used in the design phase
of the training project.

2. **SCOPE.** <br>

We will make a web store with inventory, which will allow us to carry out the control
on the entry and exit of the products that are registered in the pharmacy (famisalud
the 91), will carry out the sale of these same all this in order to be able to
improve sales and organization, in this project we will not perform the installation
nor will we maintain the software.

3. **DEFINITIONS, ACRONYMS AND ABBREVIATIONS** <br>

**SENA:** National Learning Service. <br>

**Web:** A website, portal or cybersite is a collection of web pages related to and common to an Internet domain or subdomain on the World Wide Web within the Internet. <br>

**Sofía:** Optimized System for Comprehensive Training of Active Learning. <br>

**Database:** A database is responsible for not only storing data, but also connecting them together in a logical unit. <br>

**Software:** These are the computer programs that make it possible to execute
specific tasks within a computer. For example, operating systems, applications, web browsers, games or programs. <br>

**inventory:** Inventory is the manual verification that the physical and real quantities in stock of each product in our pharmacy match the quantities
of each product registered in the management computer program.<br>

**Firewall:** It is a computer network security system that restricts Internet traffic incoming, outbound or within a private network. <br>

**Functional requirements:** Description of the capabilities or functions that the system will be able to perform. <br>

**non-functional requirements:** Constraints or features that bound the system, such as performance, user interfaces,reliability, security, portability, standards, among others.<br>

4. **PERSONAL.** <br>

|**NAME**  |**MAIL**  |**PHONE**   |
|----------|----------|------------|
|Katryn Johana gonzálezRodríguez |katrinjhoanagonzalezrodriguez@gmail.com|3022349798|
|Geronimo jose castillo martinez |jeromartinezcas21@gmail.com|3206926305|
|Thomas David Güette Marriaga|thomasmarriaga487@gmail.com|3003687800|
|Maiyer David Hernández Nieto|maiyerhernandezn@gmail.com|3046722344|
|Juan David Sarmiento Díaz|jjuandsarmiento04@gmail.com|3042285552|

5. **CURRENT SITUATION.** <br>

The company Famisalud 91 is currently managed by Duvis González who is the owner of the business, who manages the company with the help of her husband who are the only ones who manage the business. <br>

The company does not have any type of software that helps facilitate, improve and give greater efficiency to the management of the company, which leads to a deficit in several areas of it. <br>

One of the areas that may present a deficit may be the inventory area because the input and output products are registered.
manually in notebooks or other tools and this can lead to the loss of information. In the accounting area there are difficulties
When it comes to managing the accounts, because it is done manually, this can lead to inefficiency when it comes to keeping the company's accounts. <br>

Due to the difficulties that the pharmacy famisalud la 91 has been presenting, the need arises to design a web store for it that helps to improve some of the problems that the company presents. This software seeks to reduce, change or minimize as much as possible the problems that the company has been presenting, making it more efficient in most of its areas, facilitating work and improving sales. <br>

6. **PRODUCT PERSPECTIVE.** <br>

This software is expected to have an improvement in the area of ​​sales and company administration. It seeks to facilitate administrative work without reducing sales and providing greater efficiency. <br>

What will lead to the increase of clients and greater monetary income to the
business. <br>

The inventory will make the information of the input and output products better, preventing the loss of information. <br>

7. **PRODUCT FUNCTIONS.** <br>

 Inventory Record <br>
 Login<br>
 cart module <br>
 User register <br>
 payment method module <br>
 products module<br>
 main module <br>

8. **USER FEATURES.** <br>

Users will be customers, employees and administrators. <br>

Customers will have access to view and purchase the products that are available. <br>

Employees have access to the record of the products that enter and leave the pharmacy and to the section of the orders and sales made in person. <br>

The administrator will have access to sales and product registration. <br>

9. **FUNCTIONAL REQUIREMENTS.** <br>

|CODE  |Name  |
|------|------|
|RF-001|Inventory Record|
|HIGH|You must allow the administrator to show the products and the quantity with which you have each of these|
|RF-002|Login|
|HIGH|You must allow the user to log in with a type of user either (Administrator, employee or client) |
|RF-003|cart module|
|HALF|allows the user to add products to the cart and save a product without the need to take it right away|
|RF-004|User register|
|HIGH|allows the user to register in the system, as an account type (user)|
|RF-005|payment method module|
|HIGH|allows the user to select the payment method for the product|
|RF-006|products module |
|HIGH|details of each product for your organization|
|RF-007|main module|
|HIGH|In this requirement, the main page that users will access after logging in will be organized.|

10. **NON-FUNCTIONAL REQUIREMENTS** <br>

|CODE  |Name  |
|------|------|
|RNF-001|program performance |
|HIGH|The program must have the best performance, the best loading speed and the best possible performance to give good satisfaction to each of the users |
|RNF-002|Information protection |
|HIGH|The program must guarantee the security of the information that users enter|
|RNF-003|Program sustainability|
|HIGH|The program must have the ability to remain active and running at 100% if it does present a failure, it must be able to recover in the shortest possible time without affecting users in any way. |
|RNF-004|usability |
|HIGH|The interface of the program must be as clear and simple as possible so that users can use it in the best possible way.|
|RNF-005|Effectiveness |
|HIGH|The program to provide the best efficiency for greater satisfaction and for a better experience on the part of users|
|RNF-006|restrictions |
|HIGH|The program must have certain restrictions depending on the role with which the program is finished|

11. **ENTITY RELATIONSHIP MODEL** <br>

![Alt text](image.png)

12. **DIAGRAMA CASOS DE USO (UML)** <br>

![Alt text](image-1.png)
![Alt text](image-2.png)
![Alt text](Imagen_01.png)
![Alt text](image-4.png)
![Alt text](Imagen_02.png)
![Alt text](image-6.png)
![Alt text](Imagen_03.png)
![Alt text](image-8.png)
![Alt text](Imagen_04.png)
![Alt text](image-10.png)
![Alt text](Imagen_05.png)
![Alt text](image-12.png)
![Alt text](Imagen_06.png)

13. **ACTIVITIES DIAGRAM (UML)** <br>

<center>Add products to cart</center>

![Alt text](image-19.png)

<center>register user</center>

![Alt text](image-18.png)

<center>Log in</center>

![Alt text](image-17.png)

<center>Manage inventory</center>

![Alt text](image-16.png)

<center>Buy products</center>

![Alt text](image-15.png)

<center>manage products</center>

![Alt text](image-14.png)

14. **CLASS DIAGRAM (UML)** <br>

![Alt text](image-20.png)