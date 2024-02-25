# ElectroPorts & Pins Backend
This is the ElectroPorts & Pins Backend documentation. Welcome! It includes detailed instructions for installing, setting up, and using our e-commerce platform's backend.

# Project Overview
Our backend, which is the brains of our application, provides RESTful APIs for managing users, events, and authentication. It uses JSON Web Tokens (JWTs) to handle user authentication and exchange data with the database to store and retrieve data.

# Setup
    * Prerequisites :
 Before setting up the backend, ensure you have the following installed:

   * Python
   * Flask
   * Flask-RESTful
   * Flask-JWT-Extended
   * SQLAlchemy

# Installation
To install the dependencies, run the following command:

   pip install -r requirements.txt

# Running the server

   python app.py

# Dependencies
Our backend relies on the following main dependencies:

  * Flask: Micro web framework for Python.
  * Flask-RESTful: Extension for building REST APIs with Flask.
  * Flask-JWT-Extended: JSON Web Token (JWT) extension for Flask.
  * SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.

# Configuration
    * Environment Variables
Sensitive information and configuration settings should be stored in a .env file. Configure the following environment variables:

   * DATABASE_URL: Connection string for the database.
   * SECRET_KEY: Secret key for JWT encryption.

# Database
Our backend uses a relational database to store data. Here's an overview of the database:

 # Schema
Our database consists of the following tables:

 * User: Stores user details such as username, email, password hash, etc.
 * Product: Stores information about products, including brand, name, price, etc.
 * Order: Tracks orders placed by users, including products, quantities, etc.
 * Accessory: Stores details of accessories available for purchase.
 * SoundDevice: Stores information about sound devices offered in the platform.

 # Models
We use SQLAlchemy models to interact with the database. The models correspond to the tables in the database and define their structure and relationships.

 # Endpoints
Our backend provides several API endpoints for interacting with the application. Here are the main endpoints:

* User Endpoints:
  * POST /api/users/register: Register a new user.
  * POST /api/users/login: Log in an existing user.

* Product Endpoints:
  * GET /api/products: Get all products.
  * GET /api/products/<product_id>: Get details of a specific product.

* Order Endpoints:
  * GET /api/orders: Get all orders.
  * GET /api/orders/<order_id>: Get details of a specific order.
  * POST /api/orders/create: Create a new order.

For detailed information on request and response formats, refer to the API documentation.

# Authentication
Our backend uses JSON Web Tokens (JWTs) for authentication. Users receive a token upon successful login, which they include in subsequent requests to access protected endpoints.

# Error Handling
Errors in our backend are handled gracefully, with appropriate HTTP status codes and error messages returned to the client.

# Deployment
We successfuly deployed our backend on Render Platform. Once deployed, Render provided a URL where our backend application is accessible. Here is the link:
 
    https://electroports-db.onrender.com

# Developers
The backend development of this project was led by a dedicated team of developers, each contributing their unique skills and expertise to build the core functionalities of the application. Meet the talented members of our backend development team and their respective roles:

Markswell Ogutu - Backend Lead Engineer
GitHub: <a href="https://github.com/Markswell-crypto">Markswell-crypto</a>

Leon Gitonga - Assistant Backend Lead Engineer
GitHub: <a href="https://github.com/Leonkaigit">Leonkaigit</a>

Joyce Mwangi - Database Architect
GitHub: <a href="https://github.com/JOYCEmwangi8880">JOYCEmwangi8880</a>

Gerald Gicharu - Backend Engineer
GitHub: <a href="https://github.com/Gerald-GG">Gerald-GG</a>

Mercy Mwongeli - API Developer
GitHub: <a href="https://github.com/MMer-cy123">MMer-cy123</a>

Brian Mulindi - Backend Developer
GitHub: <a href="https://github.com/mulindijr">mulindijr</a>

Together, we collaborated closely, leveraging our individual strengths and skills to develop robust backend solutions, ensuring the functionality, security, and performance of the application. Our combined efforts have been instrumental in the success of our backend development efforts.

# Contributing
We welcome contributions from the community! Follow our contribution guidelines and coding standards when submitting pull requests or reporting issues.

# License
This project is licensed under the MIT License - see the LICENSE file for details.