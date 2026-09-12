**Setup
1. Create a MySQL db named "littlelemon_db" or another name of choice.

2. Create a virtual environment and install dependencies:
    (install pipenv)
    pipenv install
    pipenv shell

3. Update the database credentials in littlelemon/settings.py (or set the DB_NAME / DB_USER / DB_PASSWORD / DB_HOST / DB_PORT environment variables).

4. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Create a superuser (optional, for /admin access):
    python manage.py createsuperuser

6. Run the server:
    python manage.py runserver









**APIs TO TEST (with Insomnia, Postman or similar REST client)

User registration and authentication (Djoser):
POST http://127.0.0.1:8000/auth/users/             register a new user 
body: {"username": "user1", "password": "pass12345"}

POST http://127.0.0.1:8000/auth/token/login/        obtain auth token
body: {"username": "user1", "password": "pass12345"}

Menu:
GET    http://127.0.0.1:8000/api/menu-items/           list all menu items (public)

POST   http://127.0.0.1:8000/api/menu-items/           create a menu item (auth required)

GET    http://127.0.0.1:8000/api/menu-items/{id}/      retrieve one menu item (public)

PUT    http://127.0.0.1:8000/api/menu-items/{id}/      update a menu item (auth required)

DELETE http://127.0.0.1:8000/api/menu-items/{id}/      delete a menu item (auth required)

Table Booking API:
GET    http://127.0.0.1:8000/api/tables/              list all bookings (auth required)

POST   http://127.0.0.1:8000/api/tables/              create a booking (auth required)
body: {"name": "John Doe", "no_of_guests": 4, "booking_date": "2026-09-20"}

GET    http://127.0.0.1:8000/api/tables/{id}/          retrieve one booking (auth required)
PUT    http://127.0.0.1:8000/api/tables/{id}/          update a booking (auth required)
DELETE http://127.0.0.1:8000/api/tables/{id}/          delete a booking (auth required)