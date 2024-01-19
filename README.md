# Django Authentication Project

This is a Django project showcasing user authentication features, including signup, login, and password reset using email.

## Features

- User Signup
- User Login
- Forgot Password (Password Reset via Email)

## Technologies Used

- Django
- HTML
- CSS

## Getting Started

1. Clone the repository:

   [git clone https://github.com/ajinasanthosh1997/django-authentication-sample.git]
   
2. Install dependencies:

- pip install -r req.txt
 
3. Apply migrations:

- python manage.py migrate
  
4. Run the development server:

- python manage.py runserver
  
5. Open your web browser and visit http://localhost:8000

## Configuration
To enable email functionality, configure the following settings in settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

or

Create a .env file in the project root with the following content:

# .env file

# Email settings
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@example.com
# Add other configuration variables as needed
Replace your-email@example.com and your-email-password with your actual email credentials.

Run migrations:

- python manage.py migrate
  
Start the development server:

- python manage.py runserver
  
The project should now be running at http://localhost:8000/.

Email Configuration
To configure email settings, open the auth_project/settings.py file and update the email settings as follows:

python
Copy code
# auth_project/settings.py

from decouple import config

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') 
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
