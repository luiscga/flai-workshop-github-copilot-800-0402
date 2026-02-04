import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Leaderboard data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results ? data.results : (Array.isArray(data) ? data : []);
        console.log('Leaderboard array:', leaderboardData);
        
        setLeaderboard(leaderboardData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
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
          <p>Error loading leaderboard: {error}</p>
        </div>
      </div>
    );
  }

  const getRankBadgeClass = (rank) => {
    if (rank === 1) return 'rank-badge gold';
    if (rank === 2) return 'rank-badge silver';
    if (rank === 3) return 'rank-badge bronze';
    return 'rank-badge default';
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">Top Performers</h2>
        <span className="badge bg-warning text-dark">
          <i className="bi bi-trophy-fill"></i> Leaderboard
        </span>
      </div>
      
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <h4 className="alert-heading">No Data Available</h4>
          <p>The leaderboard will appear once activities are logged.</p>
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Rank</th>
                <th>User</th>
                <th>Team</th>
                <th>Total Calories</th>
                <th>Total Activities</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => (
                <tr key={entry._id || index}>
                  <td>
                    <span className={getRankBadgeClass(entry.rank || index + 1)}>
                      {entry.rank || index + 1}
                    </span>
                  </td>
                  <td>
                    <strong>{entry.user_name || 'N/A'}</strong>
                  </td>
                  <td>
                    <span className="badge bg-info">{entry.team_name || 'N/A'}</span>
                  </td>
                  <td>
                    <span className="badge bg-danger">{entry.total_calories || 0} cal</span>
                  </td>
                  <td>
                    <span className="badge bg-primary">{entry.total_activities || 0}</span>
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

export default Leaderboard;
