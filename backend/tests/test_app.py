# tests/test_app.py
import json
import pytest
from flask import Flask
from flask_testing import TestCase
from backend.routes import app, init_db
from backend.database import connect_db

class TestFamilyWorkoutApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['DATABASE'] = 'test_workout_app.db'
        return app

    def setUp(self):
        """Set up test database."""
        init_db()  # Initialize the test database

    def tearDown(self):
        """Clean up test database."""
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS users')
            cursor.execute('DROP TABLE IF EXISTS workouts')
            conn.commit()

    def test_register_user(self):
        """Test user registration."""
        response = self.client.post('/register', data=json.dumps({
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User registered successfully', response.data)

    def test_register_existing_user(self):
        """Test registration of an existing user."""
        # First registration
        self.client.post('/register', data=json.dumps({
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')

        # Attempt to register the same user again
        response = self.client.post('/register', data=json.dumps({
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User with this email already exists', response.data)

    def test_login_user(self):
        """Test user login."""
        # Register the user first
        self.client.post('/register', data=json.dumps({
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')

        # Attempt to log in
        response = self.client.post('/login', data=json.dumps({
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_login_wrong_password(self):
        """Test login with incorrect password."""
        # Register the user first
        self.client.post('/register', data=json.dumps({
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        }), content_type='application/json')

        # Attempt to log in with the wrong password
        response = self.client.post('/login', data=json.dumps({
            'email': 'john@example.com',
            'password': 'wrongpassword'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid email or password', response.data)

    def test_schedule(self):
        """Test workout scheduling."""
        response = self.client.get('/schedule')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alice', response.data)  # Example check

if __name__ == "__main__":
    pytest.main()
