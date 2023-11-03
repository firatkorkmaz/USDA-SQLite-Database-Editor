# USDA SQLite Database Editor
A simple database editor with READ, UPDATE and DELETE operations for USDA database in SQLite language by using Flask framework of Python.

## General Information
This project is created in 2 steps:
1. **Creating usda.sql3**: A new **usda.sql3** database file is created by running the [usda-sqlite](https://github.com/alyssaq/usda-sqlite) repository with [USDA Nutrition](https://www.ars.usda.gov/ARSUserFiles/80400535/DATA/SR/sr28/dnload/sr28asc.zip) data files.
2. **Creating the Editor**: The database editor is contained in **usda_database_editor** folder. HTML files for each food category and for main page are written along with the **crud.py** file of all the core functions.
* Detailed information can be found in **report.pdf**

## Technologies
This project is created with:
* [SQLite Browser](https://sqlitebrowser.org/dl)
* [SQLite](https://www.sqlite.org/download.html)
* Python
  * Flask Framework
* HTML

## Setup & Run
To run this program:
1. Install Flask framework:
```
pip install flask
```
2. Run the **crud.py** file in **usda_database_editor** folder with Python:
```
python crud.py
```