# Simple Flask site

Site simulation (list and detail view with images) written in Python using Flask, 
SQLAlchemy and PostgreSQL (or SQLite3) database

# Requirements:
```
Python>=3.7.3
Packages:
    Flask
    Flask-SQLAlchemy
    faker
Database:
    SQLite
```

# Initialization
Before 1st run, database should be initialized by running **init.py** module. It
will create table "items" and upload test data 
```
python init.py
```

# Run site
```
python app.py
```