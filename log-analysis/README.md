# Project: Logs Analysis

## Part of Udacity Full Stack Web Developer Nanodegree Program

## Project Description:
To build an internal reporting tool that will use information from a database of a newspaper 
website to discover which articles and authors are the most popular, and find on which
days did more then 1% of requests lead to error. The log has a database row for each time a reader 
loaded a web page. The tool don't take any input from user, it connectes to the database,
uses SQL queries to analyze the log data, and prints out the results. In this project I used 
PostgreSQL database and psycopg2 library. 


### The news database contains of tables:
- articles
- authors
- log

### Requirements
  * Install Python 3, to check version: `Python --version`
  * Install [Vagrant](https://www.vagrantup.com/) 
  * Install [Virtual Box](https://www.virtualbox.org/)
  * Download from [udacity set up file](https://github.com/udacity/fullstack-nanodegree-vm) for vagrant, 
	the file configures the vm and support software needed for this project.
  * Download the [database setup](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it, filename: newsdata.sql put this file into the vagrant directory, 
	which is shared with your virtual machine.


### Start the Virtual Machine
  * Start Terminal and navigate to the project folder.
  * cd to the vagrant directory
  * Launch the Vagrant VM inside Vagrant sub-directory in the downloaded repository 
    using command: `vagrant up` and log in command `vagrant ssh` 
  * Load the data to the database `psql -d news -f newsdata.sql
  * Run `python3 logdb.py`


