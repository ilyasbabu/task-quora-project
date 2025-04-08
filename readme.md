# Project Quora

## Features

 - User Login, Signup, Logout
 - Add Question
 - View Questions by other users
 - Like Answers
 

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ilyasbabu/task-quora-project.git
cd task-quora-project
```

### 2. Setup enviornment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Go to project directory
```bash
cd project_quora
```

### 5. Run migrations
```bash
python manage.py createsuperuser
```

### 6. Run project
```bash
python manage.py runserver
```
Then go to http://127.0.0.1:8000 ,signup and then login.