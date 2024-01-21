# All-in-One-AutoCare
This is a project for cars management system, it provides services like selling, renting, cleaning and repair for cars. 
## Project description 
The "All-in-One AutoCare Management System" is a feature-rich and adaptable Python project created to automate and simplify a number of management tasks. This complex system combines many modules to handle personnel administration, sales, rentals, repairs, cleaning schedules, and dynamic picture retrieval via external APIs. The "All-in-One AutoCare Management System" is a comprehensive system that provides effective management and enhanced operational workflows to meet the various demands of companies in the automotive sector.

# 1.
# 2. UML Design
### 2.1 Use Case Diagram:
This diagram illustrates the interactions between system actors - Salesperson, RentalManager, Cleaner, and Mechanic - and various use cases such as selling, adding, renting, reporting, cleaning, repairing, and reporting damage to cars. The arrows denote relationships, outlining the flow of actions within the car management system.

### 2.2 Class Diagram:
This visual representation showcases the structure of the system's classes, emphasizing relationships between the Car class and Customer/Employee classes. Car attributes include make, model, year, condition, price, mileage, and color. The diagram clarifies how Car inherits properties from both Customer and Employee classes.

### 2.3 Activity Diagrams:
#### Sales Activity:
The diagram outlines the steps within the car sales process, from initializing the CarSales object to managing menu options, handling user input, and updating the inventory. The loop ensures continuous operation until the user decides to exit.

#### Repair Activity:
This activity diagram delineates the steps involved in car repair, covering processes like adding cars to repair, marking them as repaired, and displaying relevant information. The loop ensures continuous operation until the user opts to close the database connection.

#### Rent Activity:
This diagram captures the sequential steps in the car rental process, including adding cars to inventory, renting them out, updating information, and managing rented cars. Similar to other activity diagrams, it operates in a loop until the user chooses to exit.

#### Clean Activity:
The diagram depicts the cleaning process, allowing users to record, mark, and schedule cleaning activities. The loop ensures ongoing operation until the user decides to exit, providing a clear overview of the cleaning management system.
### Link to view diagrams in notion:

https://www.notion.so/Software-Development-Assignmen-41a178eab49a46e19de037c326bf7ec2?pvs=4

# 3. Requirements Engineering
### A) Notion.so
This link defines the essential features for an All-in-one Auto Care Management System, encompassing sales, rental, repair, cleaning, employee management, and authentication. Using RFC 2119 terminology, it establishes mandatory (MUST), desirable (SHOULD), and optional (MAY) functionalities. The outlined modules cover inventory management, rental tracking, repair queue, cleaning records, employee details, and secure user authentication. Integration with an online payment gateway is suggested, offering a comprehensive solution for efficient autocare operations, satisfying system users.
https://www.notion.so/Q3-e411e16ea4234d1083cdb60e0e8fe477?pvs=4


prevousely I have done another requirement engineering, but it wasn't in the RFC 2119 format.
https://www.notion.so/3-1cd32c6215834de7a47b5e176b88bd90?pvs=4


### B) Jira
The all-in-one autocare Management System is described in detail in this Jira task breakdown. Various modules, including sales, renting, maintenance, cleaning, administration, and authentication, are included in the tasks. Every operation, from building database tables to putting employee interfaces in place, advances the effeciance of the system. Using Jira guarantees more effective project tracking, enabling productive teamwork and progress reporting. The development team (me) can handle required, desired, and optional features in-depth thanks to the thorough breakdown, which helps the system meet user and stakeholder expectations.

https://azuz.atlassian.net/jira/software/c/projects/AIOAS/boards/2?atlOrigin=eyJpIjoiMTMwNDZjZTFhZTI1NDMxYTk0ODEzOGFhODgzYzI5YWUiLCJwIjoiaiJ9


# 4. Analysis
### A) Checklist
This checklist was done based on my prevouse experciance with other projects and analysing their requirements. 
1.	Goals 
2.	Vision 
3.	Scope 
4.	Importance 
5.	Market analysis (Describe target, competition, similar product / service)
6.	Requirement analysis (Feasibility study, Technical feasibility, Technical feasibility, Operational feasibility, Schedule feasibility, Schedule feasibility
7.	Requirement Specification (New Proposed System, Solution Strategy, System Requirement Specification)
8.	Test Concepts / Test-Plans
9.	Milestone Management(jira)

### B) Complete checklist
The same checklist was used to write 3 pages that detail's all the points mentioned. 
https://www.notion.so/4B-20afb4d4d2b84320bc7c4facd563cd06?pvs=4
