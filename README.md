Spam_Detector

A Django-based web application to detect and manage spam contacts.
Table of Contents

    Introduction
    Features
    Technologies
    Setup
    Usage
    Folder Structure
    Contributing
    License

Introduction

The Spam Detector project aims to provide a simple interface for detecting and managing spam contacts. Users can create, search, and manage contact information, including marking certain contacts as spam.
Features

    Create and manage contact information.
    Search for contacts by name or phone number.
    Mark contacts as spam and keep track of spam counts.

Technologies

    Python 3.10
    Django 5.0.6
    postgreSQL(default database for development)

Setup
Prerequisites

Ensure you have Python 3.10 installed on your machine. You can download it from the official Python website.
Installation

    Clone the repository:

git clone https://github.com/sha-shankk/spam-Detectcor/.git
cd spam-detector

Create a virtual environment:

    python -m venv venv

Activate the virtual environment:

    On Windows:
   venv\Scripts\activate

Install the required packages:

    pip install -r requirements.txt

Apply the migrations:

    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser

Run the development server:

    python manage.py runserver

    Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

Usage

    Access the admin panel at http://127.0.0.1:8000/admin to manage contacts and users.
    Use the application to create, search, and manage contact information.
    Mark contacts as spam and view the spam count.



Contributions are welcome! Please open an issue or submit a pull request.
