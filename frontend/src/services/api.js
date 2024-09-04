// src/services/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';  // Ensure this matches your Flask server address

export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/register`, userData, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error registering user:', error);
    return { error: 'Registration failed' };
  }
};

export const loginUser = async (loginData) => {
  try {
    const response = await axios.post(`${API_URL}/login`, loginData, {
      headers: {
        'Content-Type': 'application/json',
      },
      withCredentials: true,  // Important for handling cookies/sessions
    });
    return response.data;
  } catch (error) {
    console.error('Error logging in:', error);
    return { error: 'Login failed' };
  }
};

export const fetchSchedule = async () => {
  try {
    const response = await axios.get(`${API_URL}/schedule`, {
      withCredentials: true,  // Important for handling sessions
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching schedule:', error);
    return { error: 'Failed to fetch schedule' };
  }
};
