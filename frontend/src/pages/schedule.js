// src/pages/Schedule.js
import React, { useEffect, useState } from 'react';
import { fetchSchedule } from '../services/api';

const Schedule = () => {
  const [schedule, setSchedule] = useState({});
  const [error, setError] = useState('');

  useEffect(() => {
    const getSchedule = async () => {
      const response = await fetchSchedule();
      if (response.error) {
        setError(response.error);
      } else {
        setSchedule(response);
      }
    };
    getSchedule();
  }, []);

  return (
    <div>
      <h2>Family Workout Schedule</h2>
      {error && <p>{error}</p>}
      <ul>
        {Object.entries(schedule).map(([member, workout], index) => (
          <li key={index}>{member}: {workout}</li>
        ))}
      </ul>
    </div>
  );
};

export default Schedule;
