# TaskBank

# Transaction Management API

This project provides a Django-based REST API for handling different types of operations and transactions. It includes features for creating and confirming operations, as well as integration with external gateways like ABS and CSI.

## Features

- **Create operations**: Supports creating operations with different types and amounts.
- **Confirm operations**: Allows confirming an operation after creation.
- **ABS Integration**: Handles requests and responses to the ABS gateway.
- **CSI Integration**: Manages transactions with the CSI gateway.

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git


cd your-repository


pip install -r requirements.txt


python manage.py migrate


python manage.py runserver
