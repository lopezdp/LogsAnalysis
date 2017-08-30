# Logs Analysis

> David Lopez

## About

The scope of this project is to query a large database with over a million rows which is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## To Run

### You will need:
- Python3
- PostgreSQL

### Setup
1. Install PostgreSQL 
2. Install psql CLI
3. Clone this repository
4. run `psql` in the Terminal or Command Line
5. Create a database called `news` with the following command:
  `CREATE DATABASE news;`
6. Create a user role with the following command:
  `CREATE ROLE lopezdp SUPERUSER CREATEDB CREATEROLE LOGIN;`

### To Launch & Query DB

Launch the terminal and query the database as follows:

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

To execute the program, run `python3 newsdata.py` from the command line.