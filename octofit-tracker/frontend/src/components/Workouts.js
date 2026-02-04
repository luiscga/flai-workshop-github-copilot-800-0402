import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Workouts array:', workoutsData);
        
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
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
          <p>Error loading workouts: {error}</p>
        </div>
      </div>
    );
  }

  const getDifficultyBadge = (level) => {
    const normalizedLevel = level?.toLowerCase();
    if (normalizedLevel === 'beginner' || normalizedLevel === 'easy') return 'badge bg-success';
    if (normalizedLevel === 'intermediate' || normalizedLevel === 'medium') return 'badge bg-warning text-dark';
    if (normalizedLevel === 'advanced' || normalizedLevel === 'hard') return 'badge bg-danger';
    return 'badge bg-secondary';
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">Suggested Workouts</h2>
        <span className="badge bg-warning text-dark">{workouts.length} Plans</span>
      </div>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <h4 className="alert-heading">No Workouts Available</h4>
          <p>Check back later for personalized workout suggestions!</p>
        </div>
      ) : (
        <div className="row">
          {workouts.map((workout) => (
            <div key={workout._id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <div className="d-flex justify-content-between align-items-start mb-3">
                    <h5 className="card-title mb-0">{workout.name}</h5>
                    <span className={getDifficultyBadge(workout.difficulty)}>
                      {workout.difficulty || 'N/A'}
                    </span>
                  </div>
                  <p className="card-text flex-grow-1">
                    {workout.description || 'No description available'}
                  </p>
                  <ul className="list-group list-group-flush mt-auto">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Category:</strong> 
                      <span className="badge bg-info">{workout.category || 'N/A'}</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Duration:</strong> 
                      <span className="badge bg-primary">{workout.duration} min</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Exercises:</strong> 
                      <span className="badge bg-success">{workout.exercises?.length || 0}</span>
                    </li>
                  </ul>
                  <button className="btn btn-primary mt-3 w-100">
                    Start Workout
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Workouts;
