# Interior Design Course

Welcome to my Interior Design Course, which integrates with the ForteBank API and the GetCourse API to handle payments and user registration. This project allows users to purchase courses and automatically register for them on the GetCourse platform.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Database](#database)
- [Configuration](#configuration)
- [Routes](#routes)
- [Testing](#testing)


## Introduction

This project serves as a bridge between users who want to purchase courses and two external services: ForteBank API for handling payments and the GetCourse API for registering users in courses. Users can easily purchase courses and seamlessly enroll in them on GetCourse.

## Features

- Users can purchase courses with two pricing options: base and premium.
- Automatic user registration on the GetCourse platform upon successful purchase.
- Secure payment handling through the ForteBank API.
- Easy configuration through environment variables.

## Getting Started

To get started with this project, follow these steps.

### Prerequisites

Before using this project, you need to have the following software/tools installed:

- Python
- Flask
- ForteBank API credentials (set as environment variables)
- GetCourse API credentials (set as environment variables)
- A database (e.g., PostgreSQL, SQLite) configured and set as an environment variable (e.g., DATABASE_URL)

### Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/yourproject.git
Install the required dependencies using pip.

bash
Copy code
pip install -r requirements.txt
Configure the necessary environment variables for ForteBank and GetCourse API credentials.

Run the Flask application.

```bash
python app.py
```
Access the project in your web browser at http://localhost:5000.

###Usage
Visit the project homepage.
Choose between the "Base" and "Premium" course options.
Fill in your name, surname, and email.
Click the "Purchase" button.
You will be redirected to ForteBank for payment processing.
Upon successful payment, you will be automatically registered for the selected course on GetCourse.
API Integration
This project integrates with the ForteBank and GetCourse APIs to handle payments and user registration. The key functions for these integrations are found in the forteBankApi and getCourseApi modules.

###Database
This project uses a database to store information about each purchase and user registration. The database schema is defined in the Data model, and it is configurable via the DATABASE_URL environment variable.

###Configuration
To configure the project, set the necessary environment variables for the ForteBank and GetCourse API credentials, as well as the database connection.

FORTE_LOGIN: Your ForteBank API login.
FORTE_PASSWORD: Your ForteBank API password.
ACCOUNT_NAME: Your GetCourse account name.
SECRET_KEY: Your GetCourse secret key.
DATABASE_URL: URL for your database (e.g., PostgreSQL or SQLite).
###Routes
/: Home page.
/buy: Handle course purchase.
/buy/checkPayment/<unique_id>: Check the payment status.
/buy/getCourse/<token>: Register users in GetCourse.
/about: About Us page.
###Testing
You can run tests for this project using a testing framework (e.g., pytest). Be sure to set up a test database and configure the necessary environment variables for testing.
