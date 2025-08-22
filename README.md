# Inventory Management Dashboard

A **Django-based Inventory Management System** with data visualization, allowing businesses to track product inventory, sales trends, and performance metrics efficiently. This project integrates **Plotly** and **Matplotlib** to create interactive and insightful dashboards.

## Features

- **Product Management**
  - Add, update, and delete inventory items.
  - Track quantity in stock and sales per product.
- **Interactive Dashboards**
  - Sales trend over time (line chart).
  - Best performing products (bar chart).
  - Most products in stock (pie chart).
- **User Authentication**
  - Secure login and logout using Django's built-in authentication system.
  - Role-based access (authenticated users can add or update inventory).
- **Responsive Design**
  - Mobile-friendly and modern UI for dashboard and navbar.

## Tech Stack

- **Backend:** Django 5.2, Python 3.12
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, Bootstrap, Plotly, Matplotlib
- **Data Handling:** Pandas (for converting Django QuerySets to DataFrames)

## Installation


Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate


Create a superuser (optional):
python manage.py createsuperuser


Screenshots:

Homepage==>
<img width="1842" height="634" alt="ss-1" src="https://github.com/user-attachments/assets/58b2c55c-6549-43b9-a236-401a778f5111" />


Add Item:==>
<img width="990" height="750" alt="add item" src="https://github.com/user-attachments/assets/a37af04e-2b65-4681-abde-d570bf0213cf" />


Dashboard==>
<img width="1241" height="922" alt="dashboard" src="https://github.com/user-attachments/assets/dcd3cb25-0d95-49fd-8c01-ca4c290362f1" />


Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements, bug fixes, or new features.

