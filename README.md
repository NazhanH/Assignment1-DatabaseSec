# Assignment1-DatabaseSec

## Group 10
## Members
Syed Danial Imtiaz(1221301145) 
Siddiq Ferhad(1211103095)
Nazhan Harraz(1221301122)

### Library Management System
This is a library management system that allows users to borrow and return books. The system is implemented using Python and mssql.

#### The system has the following features:
1. Add a new book
2. Remove a book
3. Borrow a book
4. Return a book
5. View all books
6. View borrowed books
7. View available books
8. Search for a book
9. View fines

#### How to run the system

**Note: Make sure you have Python and mssql installed on your system and that the database and user credentials have been setup beforehand and configured in a .env file in the src folder**

1. Install the required packages using the following command:
```pip install -r requirements.txt```
2. Go into the root directory which is the src folder
3. Make migrations using the following command:
```python manage.py makemigrations``` followed by ```python manage.py migrate```
4. Run the server using the following command:
```python manage.py runserver```
