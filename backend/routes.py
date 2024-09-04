# backend/routes.py
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from models import register_user, authenticate_user
from scheduler import generate_schedule
from config import SECRET_KEY

def register_routes(app):
    app.secret_key = SECRET_KEY
    CORS(app)

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        response = register_user(data['name'], data['email'], data['password'])
        return jsonify(response)

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        user_id = authenticate_user(data['email'], data['password'])
        if user_id:
            session['user_id'] = user_id
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    @app.route('/logout', methods=['GET'])
    def logout():
        session.pop('user_id', None)
        return jsonify({"message": "Logged out successfully"})

    @app.route('/schedule', methods=['GET'])
    def schedule():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401
        schedule = generate_schedule(user_id)
        return jsonify(schedule)

