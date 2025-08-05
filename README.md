# AuthProject

A modern Django web application with JWT authentication, featuring a beautiful responsive UI and REST API endpoints.

## Features

- **Modern UI**: Bootstrap 5 with Font Awesome icons
- **JWT Authentication**: Secure token-based authentication
- **REST API**: Clean API endpoints for authentication
- **Responsive Design**: Works perfectly on all devices
- **User Management**: Registration, login, logout functionality

## Navigation

The application includes a navigation bar with 4 main options:
- **Home**: Landing page with project overview
- **Ask**: Feature page (coming soon)
- **Login**: User authentication
- **Signup**: User registration

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   # If you have the project files, navigate to the project directory
   cd auth_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Web Interface: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## API Endpoints

### Authentication Endpoints

#### Register User
- **URL**: `POST /api/register/`
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password1": "your_password",
    "password2": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "message": "User registered successfully",
    "user": {
      "id": 1,
      "username": "your_username",
      "email": "",
      "first_name": "",
      "last_name": "",
      "date_joined": "2024-01-01T00:00:00Z"
    },
    "tokens": {
      "refresh": "refresh_token_here",
      "access": "access_token_here"
    }
  }
  ```

#### Login User
- **URL**: `POST /api/login/`
- **Description**: Authenticate user and get tokens
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Login successful",
    "user": {
      "id": 1,
      "username": "your_username",
      "email": "",
      "first_name": "",
      "last_name": "",
      "date_joined": "2024-01-01T00:00:00Z"
    },
    "tokens": {
      "refresh": "refresh_token_here",
      "access": "access_token_here"
    }
  }
  ```

#### Get User Profile
- **URL**: `GET /api/profile/`
- **Description**: Get current user profile
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
    "user": {
      "id": 1,
      "username": "your_username",
      "email": "",
      "first_name": "",
      "last_name": "",
      "date_joined": "2024-01-01T00:00:00Z"
    }
  }
  ```

#### Logout User
- **URL**: `POST /api/logout/`
- **Description**: Logout user and blacklist refresh token
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "refresh_token": "refresh_token_here"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Logout successful"
  }
  ```

#### Refresh Token
- **URL**: `POST /api/token/refresh/`
- **Description**: Get new access token using refresh token
- **Request Body**:
  ```json
  {
    "refresh": "refresh_token_here"
  }
  ```
- **Response**:
  ```json
  {
    "access": "new_access_token_here"
  }
  ```

## Project Structure

```
auth_project/
├── auth_project/          # Main project settings
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── main/                 # Main app for web views
│   ├── views.py         # Web view functions
│   ├── urls.py          # Web URL patterns
│   └── models.py        # Database models
├── api/                  # API app for REST endpoints
│   ├── views.py         # API view functions
│   ├── urls.py          # API URL patterns
│   └── serializers.py   # API serializers
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── home.html        # Homepage
│   ├── login.html       # Login page
│   ├── signup.html      # Signup page
│   └── ask.html         # Ask page
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## JWT Token Configuration

The project uses Django REST Framework Simple JWT with the following configuration:

- **Access Token Lifetime**: 60 minutes
- **Refresh Token Lifetime**: 1 day
- **Algorithm**: HS256
- **Token Type**: Bearer

## Security Features

- JWT token-based authentication
- Password validation and hashing
- CSRF protection
- Secure session management
- Token blacklisting on logout

## Future Enhancements

- Email verification
- Password reset functionality
- Social authentication (Google, Facebook, etc.)
- User profile management
- Advanced permission system
- Rate limiting
- API documentation with Swagger/OpenAPI

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License. 