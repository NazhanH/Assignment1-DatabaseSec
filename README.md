# Assignment - Database Security

## Group 10

* **Syed Danial Imtiaz** (1221301145)
* **Siddiq Ferhad** (1211103095)
* **Nazhan Harraz** (1221301122)

---

## Library Management System

This project is a **Library Management System** that allows users to borrow and return books.
The system is implemented using **Python** and **MS SQL Server**.

---

### Features

1. Add a new book
2. Remove a book
3. Borrow a book
4. Return a book
5. View all books
6. View borrowed books
7. View available books
8. Search for a book
9. View fines

---

### How to Run the System

> **Note:** Ensure that **Python**, **MS SQL Server**, and the **ODBC driver for SQL Server** are installed on your system.
> Also, make sure the database and user credentials are set up beforehand and configured in a `.env` file inside the `src` folder.

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the root directory (`src` folder).

3. Make migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```
