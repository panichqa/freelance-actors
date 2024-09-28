# Freelance Actors

This is a Django web application designed for freelance actors and event agencies to manage and assign characters (costumes) to actors. Agencies can manage characters, actors can choose costumes, and everything is integrated with user authentication.

Features
User Authentication (Login, Logout, Registration)
Actors can update their profiles and choose characters.
Agencies can manage characters and actors.
Detailed View Pages for agencies and characters.
CRUD Operations for agencies and characters.
[Check this out!
](https://freelance-actors-yg0v.onrender.com/)

### Environment Variables

Before running the project, you need to configure the required environment variables.

Copy the `env.sample` file to `.env`:

`cp env.sample .env`

Edit the `.env` file and fill in the necessary values,
such as your secret key, database credentials, and any other configurations specific to your setup.

Example
`env.sample file`

Here’s an overview of the environment variables you will find in the `env.sample` file:

`DJANGO_SECRET_KEY: A secret key used for cryptographic signing.`


`DJANGO_DEBUG: Set to True for development and False for production.
`

`DJANGO_ALLOWED_HOSTS: Hosts that your Django application can serve.
`

`DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT: Database configuration details.
`

`SESSION_ENGINE: The session backend to use (default is django.contrib.sessions.backends.db).
`

`DJANGO_TIME_ZONE: Your application's time zone.
`

`DJANGO_LANGUAGE_CODE: Default language code for the application.
`

`STATIC_URL, STATIC_ROOT: Configuration for static files.
`

`MEDIA_URL, MEDIA_ROOT: Configuration for media files.
`

`Email settings for sending emails from the application.
`
### How to Run the Project

Clone the Repository:


`git clone https://github.com/yourusername/freelance-actors.git`

Navigate to the Project Directory:

`cd freelance_actors`

Install Dependencies:

Ensure you have pip installed, then run:

`pip install -r requirements.txt`

Apply Migrations:


`python manage.py migrate`

Run the Server:

`python manage.py runserver`

Access the Website:

Open a browser and go to http://127.0.0.1:8000/.

Login to Test the Site
Use the following test credentials to log in:

Username: Kishka-durishka

Password: 123456789

For accessing the Django admin, use these credentials:

Username: admin

Password: U1s2e3r4

Test Functionality

* Agencies: Create and manage agencies.
* Characters: Add characters and assign them to agencies.
* Actors: Actors can log in and update their profiles, selecting characters based on their gender and available costumes.
Running Tests
To run the tests, use the following command:

`python manage.py test`
