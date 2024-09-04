# backend/models.py
from werkzeug.security import generate_password_hash, check_password_hash
from database import connect_db

def register_user(name, email, password):
    hashed_password = generate_password_hash(password)
    with connect_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', 
                           (name, email, hashed_password))
            conn.commit()
            return {"message": "User registered successfully"}
        except sqlite3.IntegrityError:
            return {"error": "User with this email already exists"}

def authenticate_user(email, password):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user[1], password):
            return user[0]
        else:
            return None

# Additional functions for profile management and workout logging will be added here
