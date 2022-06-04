# Concurrency schedule for employees in ACME Company
---
## Considerations
I took some considerations like:
* The time format is 24H starting with 00 and ending with 23
* The time format is hh:mm-hh:mm any other will not be considered the employee.
* The input file is called prueba.txt


## Overview of the solution

> I used ___OPP___ so that the code is better organized, easy to maintain and use     ___OPP principles___.
    The solution is divided in 3 folders: _interfaces_, _classes_ and _config_.
 * In interfaces there are two interfaces one is for data entry and one for output display. I did this with the goal of depending on abstractions and not concrete classes.
* In classes are the implementations of the data entry in this case it would be by file and the display of the results that would be in the console. There are also two schedule models, which is a class that represents an employee's schedule with attributes of the entry time and the exit time, there is also a method that returns if he shares a schedule with another employee.
* In the config folder are the days of the week that allows us to validate in the data entry class.

## Good progamming practices

* Single-Responsability Principle for methods in the classes
* Use of interfaces to depend on abstractions not concretions
* Use of clean code
* Unit tests using Pytest to test the operation of the program

## Run the program 
You need to have python version 3.9.1 and the pytest module installed.
* To run the program use python main.py
* To run the tests use pytest


- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF