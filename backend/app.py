# backend/app.py
from flask import Flask
from routes import register_routes  # Import the function to register routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

register_routes(app)  # Register routes with the app

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode

