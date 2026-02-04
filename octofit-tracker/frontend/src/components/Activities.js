import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
        console.log('Fetching activities from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Activities data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Activities array:', activitiesData);
        
        setActivities(activitiesData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>Error loading activities: {error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">Fitness Activities</h2>
        <span className="badge bg-primary">{activities.length} Total</span>
      </div>
      
      {activities.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <h4 className="alert-heading">No Activities Yet</h4>
          <p>There are no activities to display at this time.</p>
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>User</th>
                <th>Activity Type</th>
                <th>Duration (min)</th>
                <th>Distance (km)</th>
                <th>Calories</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity) => (
                <tr key={activity._id}>
                  <td>
                    <strong>{activity.user_id || 'N/A'}</strong>
                  </td>
                  <td>
                    <span className="badge bg-info">{activity.activity_type}</span>
                  </td>
                  <td>{activity.duration}</td>
                  <td>{activity.distance || 'N/A'}</td>
                  <td>
                    <span className="badge bg-success">{activity.calories} cal</span>
                  </td>
                  <td>
                    {activity.date ? new Date(activity.date).toLocaleDateString() : 'N/A'}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Activities;
