import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Teams array:', teamsData);
        
        setTeams(teamsData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchTeams();
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
          <p>Error loading teams: {error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">Fitness Teams</h2>
        <span className="badge bg-success">{teams.length} Teams</span>
      </div>
      
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <h4 className="alert-heading">No Teams Available</h4>
          <p>There are no teams created yet. Be the first to create one!</p>
        </div>
      ) : (
        <div className="row">
          {teams.map((team) => (
            <div key={team._id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{team.name}</h5>
                  <p className="card-text flex-grow-1">
                    {team.description || 'No description available'}
                  </p>
                  <div className="mt-3">
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="badge bg-primary">
                        {team.member_count || 0} Members
                      </span>
                      <small className="text-muted">
                        {new Date(team.created_at).toLocaleDateString()}
                      </small>
                    </div>
                    <button className="btn btn-outline-primary btn-sm w-100">
                      View Team
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Teams;
