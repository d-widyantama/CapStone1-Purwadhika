# CapStone1-Purwadhika
Mini HR Management System - Capstone 1 JCDS Purwadhika

Dwika Widyantama 

### Hello World!

This is my first program that I wrote and actually uploaded to github for the world to access. By saying that, this program also marks the first project that I finished as a capstone to my journey in learning and venturing into the world of Data Science. It's still few baby steps but I always believe it's the step that counts.
This project is also written for the completion of the 1st Module in Purwadhika Digital Technology scool (JC Data Science 2104) Programme. 

--- 

## Before you run the program:

### Introduction
Welcome to "Mini" HR Management System!.

This is a simple employee management program written entirely in Python V3.x. using entirely built in functions in Python, and designed to run on text-based terminal.
The tabular view on this program is written in string formating to simulate a prettier UI. The language used inside this program are mostly English and Indonesian (Well, it's mostly written when I'm in JakSel after all..)
This program allows the user to view, search, and manage employee data by adding or removing data from the initial data, and tries to demonstrate and encapsulate basic CRUD Functionality.

There are 5 main features that this program offers:
1. View Employee Data
   a. View All
   b. Filter View By Employee's Division
   c. Filter View by Gender
2. Search Employee Data - Search by Employee's name and returns detailed view
3. Delete Employee Data - Delete Employee Data by employee's unique number, features inout confirmation 
4. Add Employee Data - Adding Employee Data to initial Data, features input confirmation 

### Program OutLine

#### Data Initialization
This part contains initial data that is used throughout the program:
<img width="1344" alt="1 Initial Data" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/62a3384e-0e85-4e0e-a235-3ef462be6dd6">
The data are in dictionary format, supposed to simulate object data gotten from an api


#### Main Menu
This is the actual UI representation of the program from the Main Menu, here the user can select between available menus by entering the corresponding number from 1-5. A validation feature is added to this input to prevent user from inputting wrong format.

<img width="1340" alt="2  Main Menu" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/8b8ae6f5-5a20-4715-b435-6e386640c6ec">


#### Sub Menu 1 - Show Employee Data

Here the user can select between showing the employee data by all, filter by division or filter by gender by inputting the corresponding menu prompt (1/2/3)
By inputting 1 in the prompt, we can access the Show All employee data menu:

<img width="1247" alt="3  Submenu 1 - 1 Show All" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/4a344158-8502-4cdd-be2a-4a2b1cc5a037">


#### Sub Menu 1 - 2. Filter Employee Data By Employee Division

Here the user can filter the data based on inputted Division in a text-based prom. Capital are ignored by applying .uppper() function in the input. But, an *incorrect/unmatched division will return a blank table*.

<img width="1286" alt="4  Submenu 1 - 2 Filter Division" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/56a2fdab-4012-4577-8d0a-dde26647b6c9">


#### Sub Menu 1 - 3. Filter Employee Data By Employee Gender

Here the user can show the employee table filtered by gender, based on user input prompt of (P/L) uppercase are automatically validated, but incorrect input apart from P/L will return warning prompt and let the user input the correct prompt.

<img width="1347" alt="5  Submenu 1 - 3 Filter Gender" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/6bb6e55e-79e5-4cd5-b2ca-4639dcdfc5ee">



#### Sub Menu 2 - Search Employee Data By Employee Name

Here the user can search and dispay detaile employee data by searching with employee name. Uppercase title are ignored by default and *if the inputted name doesn't exist in the data, the program will return a blank table*.

<img width="1267" alt="6  Submenu 2 - Search Employee" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/6218a448-be1d-4c4b-9dd6-238028ded8f0">



#### Sub Menu 3 - Delete Employee Data By Employee id

Here the user can delete an employee by searching and dispay detaile employee data with employee id. Uppercase title are ignored by default and *if the inputted id doesn't exist in the data, the program will return a blank table*.
The deletion will excecuted after user inoutted the validation prompt to proceed (Y/N)

<img width="1306" alt="7  Submenu 3 - Delete Employee" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/77125de0-c448-4c4d-83d8-5d5a83988a30">


#### Sub Menu 4 - Add Employee Data

Here the user will be prompted with input prompts to input the employee data based on the attribute from Employee ID, Name, Address, Birth Date, Gender, Division.
The input prompt will return a detail on the inputted employee data and confirmation prompt, after the confirmation Y is selected, the data addition will be excexuted.
<img width="1303" alt="8  Submenu 4 - Add Employee" src="https://github.com/d-widyantama/CapStone1-Purwadhika/assets/40516898/87873643-c787-40b9-849d-62e817ae45bf">



All data used in this program are fictional, generated by faker module, any similarities from the real world data are not intentional.
Please do share some feedback on the program to help the developer improve their skill and help them through their learning journey.

-D.W-


