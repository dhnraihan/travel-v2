# Django User Management Project

This project is a Django-based 

## Features
- User registration and authentication
- Custom user model (if applicable)
- Password reset functionality
- User profile management
- Uses SQLite as the database (default)
- etc

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/dhnraihan/travel-v2.git
cd django-user
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6. Run the Development Server
```bash
python manage.py runserver
```
The project will be accessible at `http://127.0.0.1:8000/`

## Project Structure
```
travel_project/
│── / 
```

## License
This project is open-source and available under the MIT License.

