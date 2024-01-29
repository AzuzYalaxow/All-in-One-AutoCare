# All-in-One-AutoCare
This is a project for cars management system, it provides services like selling, renting, cleaning and repair for cars. 
## Project description 
The "All-in-One AutoCare Management System" is a feature-rich and adaptable Python project created to automate and simplify a number of management tasks. This complex system combines many modules to handle personnel administration, sales, rentals, repairs, cleaning schedules, and dynamic picture retrieval via external APIs. The "All-in-One AutoCare Management System" is a comprehensive system that provides effective management and enhanced operational workflows to meet the various demands of companies in the automotive sector.



# 1. GitHub
I have been using GitHub this year but so far what I have used is the browser version because it was what I started with, but so far I am learning the commands of GitHub.

Link for notion: https://slow-gum-c20.notion.site/1-158ecd3e8dea44d4afc54fb35b0979dc?pvs=4



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

Link for notion: https://slow-gum-c20.notion.site/2-41a178eab49a46e19de037c326bf7ec2?pvs=4



# 3. Requirements Engineering
### A) Notion.so
This link defines the essential features for an All-in-one Auto Care Management System, encompassing sales, rental, repair, cleaning, employee management, and authentication. Using RFC 2119 terminology, it establishes mandatory (MUST), desirable (SHOULD), and optional (MAY) functionalities. The outlined modules cover inventory management, rental tracking, repair queue, cleaning records, employee details, and secure user authentication. Integration with an online payment gateway is suggested, offering a comprehensive solution for efficient autocare operations, satisfying system users.

https://slow-gum-c20.notion.site/Q3-e411e16ea4234d1083cdb60e0e8fe477?pvs=4


prevousely I have done another requirement engineering, but it wasn't in the RFC 2119 format.

https://slow-gum-c20.notion.site/3-1cd32c6215834de7a47b5e176b88bd90?pvs=4


### B) Jira
The all-in-one autocare Management System is described in detail in this Jira task breakdown. Various modules, including sales, renting, maintenance, cleaning, administration, and authentication, are included in the tasks. Every operation, from building database tables to putting employee interfaces in place, advances the effeciance of the system. Using Jira guarantees more effective project tracking, enabling productive teamwork and progress reporting. The development team (me) can handle required, desired, and optional features in-depth thanks to the thorough breakdown, which helps the system meet user and stakeholder expectations.

https://azuz.atlassian.net/jira/software/c/projects/AIOAS/boards/2?atlOrigin=eyJpIjoiMTMwNDZjZTFhZTI1NDMxYTk0ODEzOGFhODgzYzI5YWUiLCJwIjoiaiJ9
In case Jira doesn't work this is an alternative. 
https://slow-gum-c20.notion.site/3B-b2693be1f2ca4ca4b2137d46feb40b8e?pvs=4


# 4. Analysis
### A) Checklist
This checklist was done based on my previous experience with other projects and analyzing their requirements. 
1.	Goals 
2.	Vision 
3.	Scope 
4.	Importance 
5.	Market analysis (Describe target, competition, similar product/service)
6.	Requirement analysis (Feasibility study, Technical feasibility, Operational feasibility, Schedule feasibility
7.	Requirement Specification (New Proposed System, Solution Strategy, System Requirement Specification)
8.	Test Concepts / Test-Plans
9.	Milestone Management(Jira)

### B) Complete checklist
The same checklist was used to write 3 pages that detail all the points mentioned. 

Link for the notion: https://slow-gum-c20.notion.site/4B-20afb4d4d2b84320bc7c4facd563cd06?pvs=4



# 5. DDD
Using visual event storming, I created a Domain-Driven Design (DDD) to discover and analyze important domains. mapped and displayed the relationships also used the Core Domain Chart. This strategic method facilitates informed decision-making for development by offering a clear grasp of the system's structure.

Here is the miro link : https://miro.com/app/board/uXjVN90-ZlE=/?share_link_id=47798433560



# 6. Metrics
I have used two methods of metrics for Python which were Pylint and Radon, they are straightforward to use and also have a lot of functionalities and power in terms of code.

Link for the notion: https://slow-gum-c20.notion.site/6-0c63cdb903914ec48aedd6598f73067d?pvs=4



# 7. Clean Code Development
After using Pylint and Radon it was easy to write some points of how clean my code is compared to my previous code and also previous attempts to write clean code, even though reaching 100% clean code is almost impossible it is a learning journey.

Link for the notion: https://slow-gum-c20.notion.site/7-ffb8ee33541b4f468c4d7a23f6f7f9e5?pvs=4



# 8. Build Management
Initially, Pybuilder and Pants were used to understand build management, but Pybuilder was preferred because of its superior documentation. Issues with Pybuilder's error feedback were fixed by making necessary directory adjustments. After a full day of debugging, the build was successfully finished.

Link for notion: https://slow-gum-c20.notion.site/8-0b67f9d897c942a8995987caca0bb759?pvs=4



# 9. Unit tests
I created two unittests for "sales.py" in Pybuilder by referencing some examples from youtube and also with the help of chatgpt and using the unittest library.

Link for notion: https://slow-gum-c20.notion.site/9-61b4ed79aeb9416c84a870c200f71e5d?pvs=4


# 10. IDE
"VSCode is my preferred programming editor—simple, versatile, and compatible with every language. Over 5 years, I've relied on its extensive extensions for tasks like AI and code formatting, using it for projects from my graduation work to mobile apps, websites, and cybersecurity tools. It consistently tops the list of best programming editors."

Link for notion: https://slow-gum-c20.notion.site/10-751ac898c56449cfae857c537e0d7262?pvs=4



# 11. Functional Programming
By utilizing final data structures, primarily side-effect-free functions, and higher-order functions, my work complies with functional programming standards. I use closures for modularity and encapsulation, and I use functions as arguments and return values.

Link to notion: https://slow-gum-c20.notion.site/11-cf3b48282e0649d283164825c306bbd8?pvs=4


# Personal experience
lastly, this is my personal experience and what I have encountered, it might not be much be I hope it's enough.

Link to notion: https://slow-gum-c20.notion.site/My-Personal-Experience-0f79832fe60f457ab81fddd8e95d4168?pvs=4
